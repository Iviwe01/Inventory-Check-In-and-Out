Equipment Management System
A comprehensive Python-based solution for managing and tracking equipment usage within organizations. The system provides real-time equipment check-in/out functionality with QR code verification and detailed usage history tracking.
Features

Real-time equipment check-in/out system
QR code scanning for employee verification
Equipment usage history tracking
Employee equipment monitoring
Secure Oracle APEX backend integration
User-friendly Tkinter GUI
Detailed error handling and validation
Comprehensive usage reporting

Prerequisites

Python 3.7+
OpenCV (cv2)
Tkinter
HTTP client library
Webcam/Camera for QR scanning
Oracle APEX backend setup
Required Python packages:

opencv-python
tkinter
http.client
json
urllib



Installation

Clone the repository:

bashCopygit clone https://github.com/yourusername/equipment-management.git
cd equipment-management

Install required packages:

bashCopypip install -r requirements.txt

Configure Oracle APEX connection:


Update the API endpoints in both Python files
Ensure proper network connectivity to Oracle APEX server

System Components
1. Equipment Check-in Module (Check_In_Equip.py)

QR code scanning functionality
Equipment check-in processing
Real-time status updates
Error handling and validation
User interface for check-in operations

2. Equipment Usage Viewer (View_Equip_Usage.py)

Equipment usage history tracking
Detailed usage reports
Employee equipment monitoring
Data filtering and sorting
Comprehensive usage statistics

Usage

Start the Equipment Check-in System:

bashCopypython Check_In_Equip.py

Launch the Equipment Usage Viewer:

bashCopypython View_Equip_Usage.py
API Endpoints

Check-in: apex.oracle.com/pls/apex/student101/employee/checkin
Usage Data: apex.oracle.com/pls/apex/student101/employee/checkout

Class Structure
EquipmentCheckin

Handles equipment check-in process
QR code scanning
API communication
User interface management

EmployeeEquipmentUsage

Manages equipment usage viewing
Data retrieval and display
Report generation
User interface for viewing history

Error Handling

Input validation
API connection error handling
QR code scanning verification
User feedback mechanisms
Comprehensive error messages

Security Features

QR code verification
Employee ID validation
Secure API communications
Data validation checks
Access control mechanisms

Known Issues

Camera initialization delay
API timeout on slow connections
QR code reading in low light
Limited bulk operation support

Future Enhancements

Bulk check-in/out functionality
Equipment maintenance tracking
Advanced reporting features
Mobile application support
Offline mode operations
Multi-location support

Contributing

Fork the repository
Create your feature branch
Commit your changes
Push to the branch
Submit a pull request

Troubleshooting

Camera Issues:

Ensure proper camera permissions
Check camera hardware connection
Verify OpenCV installation


API Connection:

Verify network connectivity
Check API endpoint availability
Validate API credentials



License
This project is licensed under the MIT License - see the LICENSE file for details.
Support
For support or queries:

Create an issue in the repository
Contact: andyrosecpt@gmail.com

Authors

Iviwe Mtambeka

Acknowledgments

OpenCV Team
Oracle APEX Community
Tkinter Development Team
QR Code Processing Library Contributors


Built with Python and Oracle APEX
