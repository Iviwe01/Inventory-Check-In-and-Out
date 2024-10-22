import tkinter as tk
import http.client
from urllib.parse import quote
import cv2


class EquipmentCheckin(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Equipment Check-in")
        self.geometry("400x270")
        self.configure(bg="#2e8b57")  # Background color to dark green

        # Text fields for booking id and equipment id
        booking_id_label = tk.Label(self, text="Booking ID:", bg="#2e8b57", fg="white")
        booking_id_label.pack(pady=5)
        self.booking_id_entry = tk.Entry(self, bg="white")
        self.booking_id_entry.pack(pady=5)

        equipment_id_label = tk.Label(self, text="Equipment ID:", bg="#2e8b57", fg="white")
        equipment_id_label.pack(pady=5)
        self.equipment_id_entry = tk.Entry(self, bg="white")
        self.equipment_id_entry.pack(pady=5)

        # Check-in button that will activate the Camera
        checkin_button = tk.Button(self, text="Check-in and Scan QRCode", command=self.check_in_equipment, bg="#4caf50", fg="white")
        checkin_button.pack(pady=10)

    # Scan QR code to get embedded employee ID
    def scan_qr_code(self):
        # Open the default camera
        cap = cv2.VideoCapture(0)

        while True:
            # Capture frame by frame
            ret, frame = cap.read()

            # Decode QR code from the frame
            decoded_data, _, _ = cv2.QRCodeDetector().detectAndDecode(frame)

            if decoded_data:
                employee_id = decoded_data
                cap.release()
                cv2.destroyAllWindows()
                return employee_id

            # Display the resulting frame
            cv2.imshow('QR Code Scanner', frame)

            # Allow the user to escape using 'q' key
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release the capture and close the window
        cap.release()
        cv2.destroyAllWindows()
        return None

    # Function for the check-in process
    def check_in_equipment(self):
        booking_id = self.booking_id_entry.get()
        equipment_id = self.equipment_id_entry.get()

        # Error handling for the input
        if not booking_id or not equipment_id:
            tk.messagebox.showerror("Missing Input", "Please enter both Booking ID and Equipment ID.")
            return

        try:
            equipment_id = int(equipment_id)
        except ValueError:
            tk.messagebox.showerror("Invalid Input", "Equipment ID must be a number.")
            return

        # Scan the QR code for employee ID
        employee_id = self.scan_qr_code()

        if employee_id:
            # API request for check-in and update QR code
            conn = http.client.HTTPSConnection("apex.oracle.com")
            api_url = f"/pls/apex/student101/employee/checkin?BID={quote(booking_id)}&EID={equipment_id}&EID={employee_id}"
            conn.request("POST", api_url)
            res = conn.getresponse()
            data = res.read()

            if res.status == 200:
                print('Connection Successful!')
                print(f"Booking ID: {booking_id}")
                print(f"Employee ID: {employee_id}")
                print(f"Equipment Check-in is complete, Thank You.")
            else:
                tk.messagebox.showerror("Request Failed", f"Request failed with status code: {res.status}")
        else:
            # If employee_id is invalid, API URL will run without the employee ID
            conn = http.client.HTTPSConnection("apex.oracle.com")
            api_url = f"/pls/apex/student101/employee/checkin?BID={quote(booking_id)}&EID={equipment_id}"
            conn.request("POST", api_url)
            res = conn.getresponse()
            data = res.read()

            if res.status == 200:
                print('Request Successful!')
                print(f"Booking ID: {booking_id}")
                print("Employee ID: Not detected. Move your QR Code away a bit and try again.")
            else:
                print("Request Failed", f"Request failed with status code: {res.status}")


if __name__ == "__main__":
    app = EquipmentCheckin()
    app.mainloop()
