#Admnin System SuperUser
import hashlib
import os

admin_credentials_file= 'admin_credentials.txt'
patients_file='patients.txt'
doctors_file='doctors.txt'
nurses_file='nurses.txt'
medical_records_file='medical_records.txt'


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def update_admin_credentials():
    print("Updating Admin Credentials")
    new_username=input('Enter new username: ')
    new_password=input('Enter new password: ')
    hashed_password = hash_password(new_password)
    with open(admin_credentials_file, 'w') as file:
        file.write(f"{new_username}, {hashed_password}\n")
    print('Admin Credentials Updated Successfully!')

def check_admin_credentials():
    if not os.path.exists(admin_credentials_file):
        update_admin_credentials()

def admin_login():
    print('Admin Login')
    if not os.path.exists(admin_credentials_file):
        print("No credentials found. Setup the credentials first.")
        update_admin_credentials()
        return False
    
    username=input("Enter admin username: ")
    password=input("Enter admin password: ")
    hashed_password=hash_password(password)

    with open(admin_credentials_file, 'r') as file:
        stored_username, stored_hashed_password=file.read().strip().split(',')

    if username ==stored_username.strip() and hashed_password==stored_hashed_password.strip():
        print("Login Successful")
        return True
    else:
        return False



def admin_menu():
    while True:
        print("\n--- Admin Management System ---")
        print("1. View System Summary")
        print("2. Add New Doctor")
        print("3. Add New Nurse")
        print("4. View All Patients")
        print("5. View Medical Records")
        print("6. Update Admin Credentials")
        print("7. Log Out")
        try:
            choice = int(input("Enter your choice (1-7): "))
            if choice == 1:
                print("\nSystem Summary:")
                system_summary()
            elif choice == 2:
                print("\nAdd New Doctor:")
                add_new_doctor()
            elif choice == 3:
                print("\nAdd New Nurse:")
                add_new_nurse()
            elif choice == 4:
                print("\nView All Patients:")
                view_all_patients()
            elif choice == 5:
                print("\nView Medical Records:")
                view_medical_records()
            elif choice == 6:
                update_admin_credentials()
            elif choice == 7:
                print("Logging out...")
                break
            else:
                print("Invalid choice. Please select a number between 1 and 7.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")




#Admin System Functionalities
def system_summary():
    try:
        with open(patients_file,'r') as file:
            patients= file.readlines()
        with open(doctors_file,'r') as file:
            doctors=file.readlines()
        with open(nurses_file,'r') as file:
            nurses=file.readlines()
        with open(medical_records_file,'r') as file:
            records=file.readlines()

        print(f'Total Patients: {len(patients)}')    
        print(f'Total Doctors: {len(doctors)}')    
        print(f'Total Nurses: {len(nurses)}')    
        print(f'Total Medical Records: {len(records)}') 
    except FileNotFoundError:
        print('No Records Found!')

def add_new_doctor():
    name=input("Enter the Doctor's Name: ")
    specialization=input("Enter Doctor's Speciality: ")
    contact =input("Enter doctor's contact number")

    doctor_info=f"{name},{specialization},{contact}\n"
    with open(doctors_file,'a') as file:
        file.write(doctor_info)
    print("Doctor Added Successfully!")

def add_new_nurse():
    name=input("Enter the Nurse's Name: ")
    contact =input("Enter nurse's contact number")

    nurse_info=f"{name}, {contact}\n"
    with open(nurses_file,'a') as file:
        file.write(nurse_info)
    print("Nurse Added Successfully!")

def view_all_patients():
    try:
        with open(patients_file,'r') as file:
            patients=file.readlines()
            for patient in patients:
                print(patient.strip())
    except FileNotFoundError:
        print('No Patient Records found')

def view_medical_records():
    try:
        with open(medical_records_file,'r') as file:
            records=file.readlines()
            for record in records:
                print(record.strip())
    except FileNotFoundError:
        print('No medical records found!')


#Patient Record Management System
import os

patients_data='patients_data.txt'

def load_patients():
    if not os.path.exists(patients_data):
        print(f"Warning: File '{patients_data}' does not exist. Starting with an empty list.")
        return []
    try:
        with open(patients_data,'r') as file:
            lines=file.readlines()
            patients=[]
            for line in lines:
                data= line.strip().split(',')
                if len(data)==5:
                    patients.append({
                        'name':data[0],
                        'age': data[1],
                        'gender':data[2],
                        'contact':data[3],
                        'medical_history':data[4]
                        })
            return patients
    except Exception as e:
        print(f"Error loading patient data: {e}")
        return []
    
def save_patients(patients):
    try:
        with open(patients_data, 'w') as file:
            for patient in patients:
                file.write(f"{patient['name']},{patient['age']},{patient['gender']},{patient['contact']},{patient['medical_history']}\n")
                print("Patient Added Successfully!")
    except Exception as e:
        print(f"Error saving patient data: {e}")

def add_new_patient(patients):
    print("\n--- Add New Patient ---")
    while True:
        name = input("Enter patient name: ").strip()
        if not name:
            print("Name cannot be empty. Please enter name!")
        else:
            break
    while True:
        try:
            age = int(input("Enter patient age: ").strip())
            if age <=0:
                print("Age must be a positive number. Please try again!")
            else:
                break
        except ValueError:
            print("Invalid age. Enter a valid number!")
    while True:
        gender = input("Enter patient gender: ").strip().capitalize()
        if gender not in ["Male","Female","Other"]:
            print("Invalid Input. Please Enter Male/Female or Other.")
        else:
            break
    while True:
        contact = input("Enter patient contact number: ").strip()
        if not contact.isdigit() or len(contact)<10 or len(contact)>15:
            print("Invalid Contact Number.Enter a number between 10 and 15 digits")
        else:
            break
    while True:
        medical_history = input("Enter medical history: ").strip()
        if not medical_history:
            print("Medical History cannot be empty.Please Try again")
        else:
            break

    patient={
        'name': name,
        'age': age,
        'gender': gender,
        'contact': contact,
        'medical_history': medical_history
    }
    patients.append(patient)
    save_patients(patients)
    print("New Patient Added Successfully")
    

def view_all_patients(patients):
    print("View all patients")
    if not patients:
        print("No patients found")
        return
    for idx, patient in enumerate(patients,1):
        print(f"{idx}. Name: {patient['name']}, Age: {patient['age']}, Gender: {patient['gender']}")


def search_patient(patients):
    print("Search Patients")
    search_name=input("Enter the patients name to search").strip()
    if not search_name:
        print("Search name cannot be empty. Please Try Again.")
        return
    found = False
    for patient in patients:
        if search_name.lower() in patient['name'].lower():
            print(f"Patient found: Name: {patient['name']}, Age: {patient['age']}, Gender: {patient['gender']}")
            found = True
            
    if not found:
        print(f"Patient not found for the name {search_name}")

def update_patient_details(patients):
    print("\n--- Update Patient Details ---")
    search_name = input("Enter the patient's name to update: ").strip()
    if not search_name:
        print("Name cannot be empty. Please try again.")
        return
    found = False
    for patient in patients:
        if search_name.lower() == patient['name'].lower():
            new_contact = input("Enter new contact number: ")
            new_medical_history = input("Enter new medical history: ")
            if not new_contact or not new_medical_history:
                print("Both contact number and medical history are required to update. Please try again.")
                return
            patient['contact'] = new_contact
            patient['medical_history'] = new_medical_history
            save_patients(patients)
            print(f"Patient details updated successfully for {patient['name']}.")
            found=True
            break
    if not found:
        print(f"Patient not found for name {search_name}.")

# Delete patient record
def delete_patient_record(patients):
    print("\n--- Delete Patient Record ---")
    search_name = input("Enter patient's name to delete: ")
    if not search_name:
        print("Name cannot be empty. Please try again.")
        return
    found =False
    for patient in patients:
        if search_name.lower() == patient['name'].lower():
            confirmation = input(f"Are you sure you want to delete the record of {patient['name']}? (y/n): ").strip().lower()
            if confirmation =="y":
                patients.remove(patient)
                save_patients(patients)
                print(f"Patient record deleted successfully for {search_name}.")
                found = True
            else:
                print(f"Deletion of patient record for {patient['name']} was canceled.")
            break
    if not found:
        print(f"Patient with name {search_name} not found.")

# View patient medical history
def view_patient_medical_history(patients):
    print("\n--- View Patient's Medical History ---")
    search_name = input("Enter the patient's name to view their medical history: ")
    if not search_name:
        print("Name cannot be empty. Please try again.")
        return
    found = False
    for patient in patients:
        if search_name.lower() == patient['name'].lower():
            print(f"Patient: {patient['name']}")
            print(f"Medical History: {patient['medical_history']}")
            found = True
            break
    if not found:
        print(f"Patient not found of name {search_name}.")

def patient_menu():
    patients = load_patients()  # Load existing patient data from file

    while True:
        print("\n--- Patient Management System ---")
        print("1. Add New Patient")
        print("2. View All Patients")
        print("3. Search for Patient")
        print("4. Update Patient Details")
        print("5. Delete Patient Record")
        print("6. View Patient Medical History")
        print("7. Go Back to Main Menu")

        try:
            choice = int(input("Enter your choice (1-7): "))
            if choice == 1:
                add_new_patient(patients)
            elif choice == 2:
                view_all_patients(patients)
            elif choice == 3:
                search_patient(patients)
            elif choice == 4:
                update_patient_details(patients)
            elif choice == 5:
                delete_patient_record(patients)
            elif choice == 6:
                view_patient_medical_history(patients)
            elif choice == 7:
                print("Returning to the main menu...")
                break
            else:
                print("Invalid choice. Please select a number between 1 and 7.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


#Doctor Management System
import os

doctors_data = 'doctors_data.txt'

def load_doctors():
    if not os.path.exists(doctors_data):
        return []

    try:
        with open(doctors_data, 'r') as file:
            lines = file.readlines()
            doctors = []
            for line in lines:
                data = line.strip().split(',')
                if len(data) == 4:  # name, specialization, contact, years_of_experience
                    doctors.append({
                        'name': data[0],
                        'specialization': data[1],
                        'contact': data[2],
                        'years_of_experience': data[3]
                    })
            return doctors
    except Exception as e:
        print(f"Error loading doctor data: {e}")
        return []

def save_doctors(doctors):
    try:
        with open(doctors_data, 'w') as file:
            for doctor in doctors:
                file.write(f"{doctor['name']},{doctor['specialization']},{doctor['contact']},{doctor['years_of_experience']}\n")
        print("Doctor data saved successfully!")
    except Exception as e:
        print(f"Error saving doctor data: {e}")

def add_new_doctor(doctors):
    print("\n--- Add New Doctor ---")
    while True:
        try:
            name = input("Enter doctor's name: ").strip()
            if not name:
                raise ValueError("Name cannot be empty.")
            break
        except ValueError as e:
            print(f"Error: {e}")

    while True:
        try:
            specialization = input("Enter doctor's specialization: ").strip()
            if not specialization:
                raise ValueError("Specialization cannot be empty.")
            break
        except ValueError as e:
            print(f"Error: {e}")
    
    while True:
        try:
            contact = input("Enter doctor's contact number: ").strip()
            if not contact.isdigit():
                raise ValueError("Contact number should contain only digits.")
            break
        except ValueError as e:
            print(f"Error: {e}")

    while True:
        try:
            years_of_experience = input("Enter doctor's years of experience: ").strip()
            if not years_of_experience.isdigit():
                raise ValueError("Years of experience should be a number.")
            break
        except ValueError as e:
            print(f"Error: {e}")

    doctor = {
        'name': name,
        'specialization': specialization,
        'contact': contact,
        'years_of_experience': years_of_experience
    }
    doctors.append(doctor)
    save_doctors(doctors)
    print("New doctor added successfully!")

def view_all_doctors(doctors):
    print("\n--- List of All Doctors ---")
    if not doctors:
        print("No doctor records available.")
        return

    for i, doctor in enumerate(doctors, start=1):
        print(f"{i}. Name: {doctor['name']}, Specialization: {doctor['specialization']}, Contact: {doctor['contact']}")


def search_doctor(doctors):
    print("Search for doctor:")
    search_name = input("Enter the doctor's name to search: ").strip().lower()
    found = False
    for doctor in doctors:
        if search_name in doctor['name'].lower():
            print(f"Doctor found: Name: {doctor['name']}, Specialization: {doctor['specialization']}, Contact: {doctor['contact']}, Experience: {doctor['years_of_experience']} years")
            found = True
            break
    if not found:
        print("Doctor not found.")

def update_doctor_details(doctors):
    print("\n--- Update Doctor Details ---")
    search_name = input("Enter the doctor's name to update: ").strip()
    for doctor in doctors:
        if search_name.lower() == doctor['name'].lower():
            while True:
                try:
                    new_contact = input("Enter new contact number: ").strip()
                    if not new_contact.isdigit():
                        raise ValueError("Contact number should contain only digits.")
                    break
                except ValueError as e:
                    print(f"Error: {e}")

            while True:
                try:
                    new_specialization = input("Enter new specialization: ").strip()
                    if not new_specialization:
                        raise ValueError("Specialization cannot be empty.")
                    break
                except ValueError as e:
                    print(f"Error: {e}")

            while True:
                try:
                    new_experience = input("Enter new years of experience: ").strip()
                    if not new_experience.isdigit():
                        raise ValueError("Years of experience should be a number.")
                    break
                except ValueError as e:
                    print(f"Error: {e}")

            doctor['contact'] = new_contact
            doctor['specialization'] = new_specialization
            doctor['years_of_experience'] = new_experience
            save_doctors(doctors)
            print("Doctor details updated successfully.")
            return
    print("Doctor not found.")

def delete_doctor_record(doctors):
    print("\n--- Delete Doctor Record ---")
    search_name = input("Enter the doctor's name to delete: ").strip()

    for doctor in doctors:
        if search_name.lower() == doctor['name'].lower():
            doctors.remove(doctor)
            save_doctors(doctors)
            print("Doctor record deleted successfully.")
            return
    print("Doctor not found.")


def doctor_menu():
    doctors = load_doctors()  # Load existing doctor data from file

    while True:
        print("\n--- Doctor Management System ---")
        print("1. Add New Doctor")
        print("2. View All Doctors")
        print("3. Search for Doctor")
        print("4. Update Doctor Details")
        print("5. Delete Doctor Record")
        print("6. Go Back to Main Menu")

        try:
            choice = int(input("Enter your choice (1-6): "))
            if choice == 1:
                add_new_doctor(doctors)
            elif choice == 2:
                view_all_doctors(doctors)
            elif choice == 3:
                search_doctor(doctors)
            elif choice == 4:
                update_doctor_details(doctors)
            elif choice == 5:
                delete_doctor_record(doctors)
            elif choice == 6:
                print("Returning to the main menu...")
                break
            else:
                print("Invalid choice. Please select a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


# Nurse Management System
import os

nurses_data = 'nurses_data.txt'

# Load nurses data from file
def load_nurses():
    if not os.path.exists(nurses_data):
        return []

    try:
        with open(nurses_data, 'r') as file:
            lines = file.readlines()
            nurses = []
            for line in lines:
                data = line.strip().split(',')
                if len(data) == 4:  # name, department, contact, shift
                    nurses.append({
                        'name': data[0],
                        'department': data[1],
                        'contact': data[2],
                        'shift': data[3]
                    })
            return nurses
    except Exception as e:
        print(f"Error loading nurse data: {e}")
        return []

# Save nurses data to file
def save_nurses(nurses):
    try:
        with open(nurses_data, 'w') as file:
            for nurse in nurses:
                file.write(f"{nurse['name']},{nurse['department']},{nurse['contact']},{nurse['shift']}\n")
        print("Nurse data saved successfully!")
    except Exception as e:
        print(f"Error saving nurse data: {e}")

# Add a new nurse
def add_new_nurse(nurses):
    print("\n--- Add New Nurse ---")
    while True:
        try:
            name = input("Enter nurse's name: ").strip()
            if not name:
                raise ValueError("Name cannot be empty.")
            break
        except ValueError as e:
            print(f"Error: {e}")

    while True:
        try:
            department = input("Enter nurse's department: ").strip()
            if not department:
                raise ValueError("Department cannot be empty.")
            break
        except ValueError as e:
            print(f"Error: {e}")

    while True:
        try:
            contact = input("Enter nurse's contact number: ").strip()
            if not contact.isdigit():
                raise ValueError("Contact number should contain only digits.")
            break
        except ValueError as e:
            print(f"Error: {e}")

    while True:
        try:
            shift = input("Enter nurse's shift (e.g., Morning/Night): ").strip()
            if not shift:
                raise ValueError("Shift cannot be empty.")
            break
        except ValueError as e:
            print(f"Error: {e}")

    nurse = {
        'name': name,
        'department': department,
        'contact': contact,
        'shift': shift
    }
    nurses.append(nurse)
    save_nurses(nurses)
    print("New nurse added successfully!")

# View all nurses
def view_all_nurses(nurses):
    print("\n--- List of All Nurses ---")
    if not nurses:
        print("No nurse records available.")
        return

    for i, nurse in enumerate(nurses, start=1):
        print(f"{i}. Name: {nurse['name']}, Department: {nurse['department']}, Contact: {nurse['contact']}, Shift: {nurse['shift']}")

# Search for a nurse
def search_nurse(nurses):
    print("\n--- Search Nurse ---")
    search_name = input("Enter the nurse's name to search: ").strip().lower()
    found = False
    for nurse in nurses:
        if search_name in nurse['name'].lower():
            print(f"Found Nurse: Name: {nurse['name']}, Department: {nurse['department']}, Contact: {nurse['contact']}, Shift: {nurse['shift']}")
            found = True
    if not found:
        print("Nurse not found.")

# Update nurse details
def update_nurse_details(nurses):
    print("\n--- Update Nurse Details ---")
    search_name = input("Enter the nurse's name to update: ").strip().lower()
    for nurse in nurses:
        if search_name == nurse['name'].lower():
            while True:
                try:
                    new_contact = input("Enter new contact number: ").strip()
                    if not new_contact.isdigit():
                        raise ValueError("Contact number should contain only digits.")
                    break
                except ValueError as e:
                    print(f"Error: {e}")

            while True:
                try:
                    new_department = input("Enter new department: ").strip()
                    if not new_department:
                        raise ValueError("Department cannot be empty.")
                    break
                except ValueError as e:
                    print(f"Error: {e}")

            while True:
                try:
                    new_shift = input("Enter new shift (e.g., Morning/Night): ").strip()
                    if not new_shift:
                        raise ValueError("Shift cannot be empty.")
                    break
                except ValueError as e:
                    print(f"Error: {e}")

            nurse['contact'] = new_contact
            nurse['department'] = new_department
            nurse['shift'] = new_shift
            save_nurses(nurses)
            print("Nurse details updated successfully.")
            return
    print("Nurse not found.")

# Delete nurse record
def delete_nurse_record(nurses):
    print("\n--- Delete Nurse Record ---")
    search_name = input("Enter the nurse's name to delete: ").strip().lower()

    for nurse in nurses:
        if search_name == nurse['name'].lower():
            nurses.remove(nurse)
            save_nurses(nurses)
            print("Nurse record deleted successfully.")
            return
    print("Nurse not found.")

# Nurse Management Menu
def nurse_menu():
    nurses = load_nurses()  # Load existing nurse data from file

    while True:
        print("\n--- Nurse Management System ---")
        print("1. Add New Nurse")
        print("2. View All Nurses")
        print("3. Search for Nurse")
        print("4. Update Nurse Details")
        print("5. Delete Nurse Record")
        print("6. Go Back to Main Menu")

        try:
            choice = int(input("Enter your choice (1-6): "))
            if choice == 1:
                add_new_nurse(nurses)
            elif choice == 2:
                view_all_nurses(nurses)
            elif choice == 3:
                search_nurse(nurses)
            elif choice == 4:
                update_nurse_details(nurses)
            elif choice == 5:
                delete_nurse_record(nurses)
            elif choice == 6:
                print("Returning to the main menu...")
                break
            else:
                print("Invalid choice. Please select a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


#Medical Record management system
import os

def add_medical_record():
    print("\n--- Add Medical Record ---")
    
    # Input patient details
    patient_name = input("Enter patient's name: ").strip()
    diagnosis = input("Enter diagnosis: ").strip()
    treatment = input("Enter treatment: ").strip()
    date = input("Enter date (e.g., YYYY-MM-DD): ").strip()
    
    # Append to file
    try:
        with open(medical_records_file, 'a') as file:
            file.write(f"{patient_name},{diagnosis},{treatment},{date}\n")
        print("Medical record added successfully!")
    except Exception as e:
        print(f"Error saving record: {e}")

def view_medical_records():
    print("\n--- View Medical Records ---")
    
    if not os.path.exists(medical_records_file):
        print("No medical records found.")
        return

    try:
        with open(medical_records_file, 'r') as file:
            records = file.readlines()
            if not records:
                print("No medical records found.")
                return
            print("\nMedical Records:")
            for record in records:
                patient_name, diagnosis, treatment, date = record.strip().split(',')
                print(f"Patient: {patient_name}, Diagnosis: {diagnosis}, Treatment: {treatment}, Date: {date}")
    except Exception as e:
        print(f"Error reading records: {e}")

def delete_medical_record():
    print("\n--- Delete Medical Record ---")
    
    if not os.path.exists(medical_records_file):
        print("No medical records found.")
        return

    search_name = input("Enter the patient's name to delete records: ").strip().lower()
    updated_records = []

    try:
        with open(medical_records_file, 'r') as file:
            records = file.readlines()
        
        for record in records:
            if search_name not in record.split(',')[0].lower():
                updated_records.append(record)
        
        with open(medical_records_file, 'w') as file:
            file.writelines(updated_records)

        print("Records updated. Specified records deleted if found.")
    except Exception as e:
        print(f"Error deleting record: {e}")

#Medical records menu

def medical_records_menu():
    while True:
        print("\n--- Medical Records Management ---")
        print("1. Add Medical Record")
        print("2. View Medical Records")
        print("3. Delete Medical Record")
        print("4. Go Back to Main Menu")
        
        try:
            choice = int(input("Enter your choice (1-4): "))
            if choice == 1:
                add_medical_record()
            elif choice == 2:
                view_medical_records()
            elif choice == 3:
                delete_medical_record()
            elif choice == 4:
                print("Returning to Main Menu...")
                break
            else:
                print("Invalid choice. Please select 1-4.")
        except ValueError:
            print("Invalid input. Please enter a number.")


#Login Page

def main_menu():
    print("Welcome to the Medical Record Management System")
    print("1. Admin Management System")
    print("2. Patient Management System")
    print("3. Doctor Management System")
    print("4. Nurses Management System")
    print("5. Medical Records")
    print("6. Exit") 


def main_login_page():
        main_menu()
        while True:
            try:
                choice = int(input("Enter your choice from (1-8): "))

                if choice == 1:
                    print('Admin Management System Selected')
                    if admin_login():
                        admin_menu()
                    else:
                        print('Access denied. Returning to main menu')
                elif choice == 2:
                    print('Patient Management System Selected')
                    patient_menu()
                elif choice == 3:
                    print('Doctor Management System Selected')
                    doctor_menu()
                elif choice == 4:
                    print('Nurses Management System Selected')
                    nurse_menu()
                elif choice == 5:
                    print('Medical Records Selected')
                    medical_records_menu()
                elif choice == 6:
                    confirm = input("Are you sure you want to exit? (yes/no): ").lower()
                    if confirm == "yes":
                        print("Exiting the System")
                        break
                else:
                    print('Invalid Choice. Enter a number between 1 and 8')
            except ValueError:
                print('Invalid Input. Enter a number from 1-8')
                    


main_login_page()
