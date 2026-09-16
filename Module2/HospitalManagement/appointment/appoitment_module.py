'''3. Appointment Management Package

Create a package named "appointment".

Create module:
appointment_module.py


Implement:


a) book_appointment()

Take appointment details:

- Appointment ID
- Patient ID
- Doctor ID
- Appointment Date
- Appointment Time


Store appointment information.


b) show_appointments()

Display all booked appointments.


--------------------------------------------------'''

Appoitment=[]
def book_appointment():
    id=input("Appointment ID:")
    p_id=input("Patient ID:")
    d_id=input("Doctor ID: ")
    date=input("Appointment Date: ")
    time=input("Appointment Time: ")
    appoitment_details={}
    appoitment_details[id]={
        "Patient ID":p_id,
        "Doctor ID":d_id,
        "Appointment Date":date,
        "Appointment Time":time
    }
    Appoitment.appent(appoitment_details)
    print("Stored appoitment Information")

def show_appointments():
    if len(Appoitment)==0:
        print("No Appoitment Added")
    else:
        print("---Appoitment Details----")
        for appoit in Appoitment:
            for appoit,details in appoit.items:
                print("Appointment ID:",appoit)
                print("Patient ID:",details["Patient ID"])
                print("Doctor ID:",details["Doctor ID"])
                print("Appointment Date:",details["Appointment Date"])
                print("Appointment Time:",details["Appointment Time"])
                print("-----------------------------")
            
        

