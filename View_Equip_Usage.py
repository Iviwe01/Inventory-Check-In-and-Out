import tkinter as tk
import tkinter.ttk as ttk
import http.client
import json
from tkinter import messagebox


class EmployeeEquipmentUsage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("View Equipment Usage")
        self.geometry("800x600")
        self.configure(bg="#2e8b57")  # Background color to dark green

        # Styling
        style = ttk.Style()
        style.theme_use("clam")

        # Frame of Header
        header_frame = ttk.Frame(self, padding=20)
        header_frame.pack(fill=tk.X)
        header_label = ttk.Label(header_frame, text="View Equipment Usage", font=("Arial", 18, "bold"))
        header_label.pack()

        # Text field frame
        input_frame = ttk.Frame(self, padding=20)
        input_frame.pack(fill=tk.X)
        input_label = ttk.Label(input_frame, text="Enter Employee ID:", font=("Arial", 14))
        input_label.pack(side=tk.LEFT, padx=10)
        self.employee_id_input = ttk.Entry(input_frame, font=("Arial", 14))
        self.employee_id_input.pack(side=tk.LEFT, padx=10)
        submit_button = ttk.Button(input_frame, text="Submit", command=self.get_equipment_usage,
                                   style="Accent.TButton")
        submit_button.pack(side=tk.LEFT, padx=10)

        # Table with Equipment details
        result_frame = ttk.Frame(self, padding=20)
        result_frame.pack(fill=tk.BOTH, expand=True)
        result_label = ttk.Label(result_frame, text="Equipment Usage:", font=("Arial", 14))
        result_label.pack(anchor=tk.NW)

        # Columns for the table
        columns = ("No", "BookingID", "EquipmentID", "CheckOutDate", "CheckInDate")
        self.equipment_treeview = ttk.Treeview(result_frame, columns=columns, show="headings")
        self.equipment_treeview.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.equipment_treeview.heading("No", text="No.")
        self.equipment_treeview.column("No", width=50, anchor=tk.CENTER)
        self.equipment_treeview.heading("BookingID", text="Booking ID")
        self.equipment_treeview.column("BookingID", width=150, anchor=tk.CENTER)
        self.equipment_treeview.heading("EquipmentID", text="Equipment ID")
        self.equipment_treeview.column("EquipmentID", width=150, anchor=tk.CENTER)
        self.equipment_treeview.heading("CheckOutDate", text="Check Out Date")
        self.equipment_treeview.column("CheckOutDate", width=150, anchor=tk.CENTER)
        self.equipment_treeview.heading("CheckInDate", text="Check In Date")
        self.equipment_treeview.column("CheckInDate", width=150, anchor=tk.CENTER)

        # Customization of GUI
        style.configure("Accent.TButton", font=("Arial", 14), foreground="white", background="#2e8b57")
        style.map("Accent.TButton", background=[("active", "#2e8b57")])

    def get_equipment_usage(self):
        employee_id = self.employee_id_input.get()

        # Validate text inputs
        if not employee_id.isdigit():
            messagebox.showerror("Invalid Input", "Invalid employee ID. Please enter a numeric value.")
            return

        # Clear previous result
        for item in self.equipment_treeview.get_children():
            self.equipment_treeview.delete(item)

        # Connect to the API
        conn = http.client.HTTPSConnection("apex.oracle.com")
        api_url = "https://apex.oracle.com/pls/apex/student101/employee/checkout"
        try:
            conn.request("GET", api_url)
            response = conn.getresponse()

            if response.status == 200:
                data = response.read()
                equipment_manager = json.loads(data.decode('utf-8'))

                if 'items' in equipment_manager:
                    employee_equipment_usage = []
                    equipment_found = False
                    counter = 1
                    for equipment in equipment_manager['items']:
                        if int(equipment.get("employeeid", -1)) == int(employee_id):
                            equipment_found = True
                            bookingid = equipment.get("bookingid", "N/A")
                            equipmentid = equipment.get("equipmentid", "N/A")
                            checkoutdate = equipment.get("checkoutdate", "N/A")
                            checkindate = equipment.get("checkindate", "N/A")
                            self.equipment_treeview.insert("", "end", values=(
                            counter, bookingid, equipmentid, checkoutdate, checkindate))
                            counter += 1

                    if not self.equipment_treeview.get_children():
                        if equipment_found:
                            messagebox.showinfo("No Equipment Usage",
                                                "No equipment usage found for the given employee ID.")
                        else:
                            messagebox.showerror("Invalid Employee ID",
                                                 "Invalid employee ID. Please re-enter a correct Employee ID.")
                else:
                    messagebox.showerror("API Error", "The item is not present in the API endpoint.")
            else:
                messagebox.showerror("Connection Error", f"Connection failed. Status code: {response.status}")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

        finally:
            print('Connection Successful!')
            print('Employee ID: ' + employee_id)
            print('Equipment Viewing Complete, Thank You.')
            conn.close()


if __name__ == "__main__":
    app = EmployeeEquipmentUsage()
    app.mainloop()