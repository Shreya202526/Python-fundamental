'''
Requirements:

1. Patient Management Package

Create a package named "patient".

Create module:
patient_module.py


Implement the following functions:

a) add_patient()

Take patient details from user:

- Patient ID
- Patient Name
- Age
- Gender
- Disease
- Mobile Number


Store patient information using list and dictionary.


b) display_patients()

Display all registered patients.


c) search_patient()

Search patient details using Patient ID.


----------------------------------'''
Patient=[]
def add_patient():
    patient_details={}
    patient_id=int(input("Patient ID:"))
    patient_name=input("Patient Name: ")
    age=int(input("Age: "))
    gender=input("Gender: ")
    disease=input("Disease: ")
    mobile_no=input("Mobile no: ")
    patient_details[patient_id]={
        "Patient Name":patient_name,
        "Age":age,
        "Gender":gender,
        "Disease":disease,
        "Mobile Number":mobile_no
    }
    Patient.append(patient_details)
    print("Patient Added Successfully")

def display_patients():
    if len(Patient)==0:
        print("No patients")
    else:
        print("====Patients Details====")
        for patient in Patient:
         for patient,details in patient.items():
            print("Patient ID:",patient)
            print("Patient Name:", details["Patient Name"])
            print("Age:", details["Age"])
            print("Gender:", details["Gender"])
            print("Disease:",details["Disease"])
            print("Mobile Number:", details["Mobile Number"])
            print("------------------------------------")
def search_patient():
    patient_id=int(input("Enter the patient id: "))
    for patient in Patient:
     if patient_id in patient:
         details=patient[patient_id]
         print("Patient Found")
         print("Patient ID:", patient_id)
         print("Patient Name:", details["Patient Name"])
         print("Age:", details["Age"])
         print("Gender:", details["Gender"])
         print("Disease:", details["Disease"])
         print("Mobile Number:", details["Mobile Number"])

         return

    print("Patient Not Found")