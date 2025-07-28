# Hospital Management System

The Hospital Management System is a console-based application developed in Python designed to facilitate the efficient management of various aspects within a hospital environment. It provides functionalities for administrators, patient records, doctor information, nurse details, and medical record keeping, ensuring organized and accessible data management through file I/O.

# Features:

# Admin System:

Secure admin login with password hashing (SHA-256) for authentication.

Ability to update admin credentials.

View system summaries, including total patients, doctors, nurses, and medical records.

Directly add new doctor and nurse entries.

View all registered patients and medical records.

# Patient Management System:

Add new patient records with details such as name, age, gender, contact, and medical history.

View a comprehensive list of all registered patients.

Search for specific patients by name.

Update existing patient details, including contact information and medical history.

Delete patient records from the system.

View a patient's complete medical history.

# Doctor Management System:

Add new doctor profiles, including name, specialization, contact, and years of experience.

View a directory of all doctors.

Search for doctors by name.

Update doctor contact details, specialization, and experience.

Delete doctor records.

# Nurse Management System:

Add new nurse profiles with details like name, department, contact, and shift.

View a list of all registered nurses.

Search for nurses by name.

Update nurse contact details, department, and shift.

Delete nurse records.

# Medical Records Management System:

Add new medical records for patients, including diagnosis, treatment, and date.

View all stored medical records.

Delete medical records based on patient name.

# Technical Details:

Language: Python

Data Storage: Persistent data storage using flat files (e.g., patients.txt, doctors.txt, nurses.txt, medical_records.txt, admin_credentials.txt).

Security: Basic password hashing (SHA-256) implemented for admin login.

Structure: Modular design with functions grouped by their respective management areas (Admin, Patient, Doctor, Nurse, Medical Records).

# How to Run the Application:

# Prerequisites:

Python 3.x installed on your system.

# Clone the Repository:

Bash

git clone https://github.com/yourusername/Hospital-Management-System.git
cd Hospital-Management-System
Run the Application:

Bash

python "hms_main.py"


# Future Enhancements:

Implement a graphical user interface (GUI) using libraries like Tkinter or PyQt.

Integrate with a database (e.g., SQLite, MySQL) for more robust data management.

Add user roles and permissions for different staff members (e.g., doctors can only view their patients' records).

Implement appointment scheduling.

Enhance search functionalities with more criteria.

Error handling for file operations.
