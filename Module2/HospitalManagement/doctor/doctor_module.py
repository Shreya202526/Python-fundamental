'''2. Doctor Management Package

Create a package named "doctor".

Create module:
doctor_module.py


Implement the following functions:


a) add_doctor()

Take doctor details:

- Doctor ID
- Doctor Name
- Specialization
- Experience
- Consultation Fees


store doctor information using list and dictionary.


b) display_doctors()

Display all doctor details.
'''

Doctor=[]
def add_doctor():
    doctor_details={}
    id=int(input("Doctor ID: "))
    name=input("Enter the Doctor Name: ")
    specilization=input("Specilization: ")
    experience=input("Experience: ")
    consultation=input("Consultation Fees: ")
    doctor_details[id]={
        "Doctor Name":name,
        "Specialization":specilization,
        "Experience":experience,
        "Consultation Fees":consultation
    }
    Doctor.append(doctor_details)

def display_doctors():
    if len(Doctor)==0:
        print("No Doctor Added")
    else:
        print("---Doctors Details----")
        for doctor in Doctor:
            for doctor,details in doctor.items:
                print("Doctor ID:",doctor)
                print("Doctor Name:",details["Doctor Name"])
                print("Specialization:",details["Specialization"])
                print("Experience:",details["Experience"])
                print("Consultation Fees:",details["Consultation Fees"])
                print("-----------------------------")
            
        





