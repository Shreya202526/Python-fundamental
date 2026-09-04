'''1.ASSIGNMENT: HOSPITAL PATIENT RECORD MANAGEMENT SYSTEM:--

A multi-specialty hospital is currently maintaining patient records manually in registers. As the number of patients is increasing, it has become difficult to search, update, and manage records efficiently.

The hospital management has decided to develop a simple Patient Record Management System using Python. The system should store patient information in a nested dictionary where:

Key → Patient ID
Value → Dictionary containing patient details

Each patient record should contain:

Patient Name
Age
Gender
Disease
Doctor Name
Sample Data Structure
{
101:{
    "name":"Ajay",
    "age":35,
    "gender":"Male",
    "disease":"Fever",
    "doctor":"Dr. Sharma"
},
102:{
    "name":"Ravi",
    "age":42,
    "gender":"Male",
    "disease":"Diabetes",
    "doctor":"Dr. Gupta"
}
}
Menu Driven Program

Display the following menu repeatedly until the user chooses Exit.

=====================================
 HOSPITAL PATIENT MANAGEMENT SYSTEM
=====================================

1. Add New Patient
2. Search Patient
3. Update Patient Disease
4. Delete Patient Record
5. Display All Patients
6. Count Total Patients
7. Display Patients By Disease
8. Display Oldest Patient
9. Display Youngest Patient
10. Exit

Functional Requirements
1. Add New Patient

Accept the following information from the user:

Patient ID
Patient Name
Age
Gender
Disease
Doctor Name

Store the record in the nested dictionary.

Validation:
If the Patient ID already exists, display:

Patient ID already exists.

2. Search Patient

Accept Patient ID from the user.

If the patient exists, display complete information.

Sample Output

Patient ID : 101
Name       : Ajay
Age        : 35
Gender     : Male
Disease    : Fever
Doctor     : Dr. Sharma

If Patient ID is not found:

Patient Record Not Found

3. Update Patient Disease

Accept Patient ID.

If found:

Ask for new disease.
Update the disease information.

Sample Output

Disease Updated Successfully
4. Delete Patient Record

Accept Patient ID.

If found:

Remove the patient record.

Sample Output

Patient Record Deleted Successfully

Otherwise:

Patient Not Found
5. Display All Patients

Display all patient records in a formatted manner.

Sample Output

--------------------------------
Patient ID : 101
Name       : Ajay
Age        : 35
Disease    : Fever
Doctor     : Dr. Sharma
--------------------------------

Patient ID : 102
Name       : Ravi
Age        : 42
Disease    : Diabetes
Doctor     : Dr. Gupta
6. Count Total Patients

Display the total number of patients currently stored.

Sample Output

Total Patients : 25
7. Display Patients By Disease

Accept a disease name from the user.

Display all patients suffering from that disease.

Sample Output

Enter Disease : Fever

101  Ajay
108  Aman
115  Neha

If no patient is found:

No Patient Found
8. Display Oldest Patient

Find and display the patient having the highest age.

Sample Output

Oldest Patient Details

Patient ID : 110
Name       : Ravi
Age        : 68
Disease    : Diabetes
Doctor     : Dr. Gupta
9. Display Youngest Patient

Find and display the patient having the minimum age.

Sample Output

Youngest Patient Details

Patient ID : 121
Name       : Riya
Age        : 4
Disease    : Viral Fever
Doctor     : Dr. Mehta
10. Exit

Terminate the application.

Sample Output

Thank You For Using Hospital Patient Management System
'''


patient={}
while True:
 print("=====================================")
 print("HOSPITAL PATIENT MANAGEMENT SYSTEM")
 print("=====================================")
 print("1. Add New Patient")
 print("2. Search Patient")
 print("3. Update Patient Disease")
 print("4. Delete Patient Record")
 print("5. Display All Patients")
 print("6. Count Total Patients")
 print("7. Display Patients By Disease")
 print("8. Display Oldest Patient")
 print("9. Display Youngest Patient")
 print("10. Exit")
 choice=int(input("Enter your choice: "))
 match choice:
      case 1:
            n=int(input("Enter the number of Patient: "))
            for i in range(n):
              id=int(input("Enter the Patient ID: "))
              Name=input("Enter the name of the patient:")
              Age=int(input("Enter the age of Patient:"))
              Gender=input("Enter the Gender:")
              Disease=input("Enter the Disease:")
              Doctor_Name=input("Enter the doctor name")
              if id not in patient:
               patient[id]={
                 "name":Name,
                 "age":Age,
                 "gender":Gender,
                 "disease":Disease,
                 "doctor":Doctor_Name
                }
              print("Data Add successfully")

            else:
               print("Data Already Exists")

      case 2:
        id=int(input("Enter The patient id: "))
        if id in patient:
           print("Patient ID :", id)
           print("Name       :", patient[id]["name"])
           print("Age        :", patient[id]["age"])
           print("Gender     :", patient[id]["gender"])
           print("Disease    :", patient[id]["disease"])
           print("Doctor     :", patient[id]["doctor"])
        else:
            print("Patient id not exists!!!")
      case 3:
        id=int(input("Enter the patient id: "))
        if id in patient:
           new_disease=input("Enter new disease:")
           patient[id]["disease"]=new_disease
           print("Updated Successfully_____")
           print(patient)
        else:
           print("Patient Id Not found")
      case 4:
         id=int(input("Enter the patient id"))     
         if id in patient:
            del patient[id]
            print(patient)
            print("Patient Record removed Successfully")
         else:
            print("patient id not found")
      case 5:
         for k,v in patient.items():
                 print("---------------------------------")
                 print("Patient ID :", k)
                 print("Name       :", v["name"])
                 print("Age        :", v["age"])
                 print("Gender     :", v["gender"])
                 print("Disease    :", v["disease"])
                 print("Doctor     :", v["doctor"]) 
      case 6:   
        print("Total patients:",len(patient)) 
      case 7:
           disease = input("Enter Disease: ")
           found = False

           for k, v in patient.items():
            if v["disease"].lower() == disease.lower():
              print(k, v["name"])
              found = True

           if found == False:
             print("No Patient Found")

      case 8:
         oldest_age=0
         oldest_id=None       
         for k,v in patient.items():
            if v["age"]>=oldest_age:
               oldest_age=v["age"]
               oldest_id=k
         print("Oldest Patient Details")
         print("Patient ID :", oldest_id)
         print("Name       :", patient[oldest_id]["name"])
         print("Age        :", patient[oldest_id]["age"])
         print("Disease    :", patient[oldest_id]["disease"])
         print("Doctor     :", patient[oldest_id]["doctor"])

      case 9:
       youngest_age=999
       youngest_id=None
       for k,v in patient.items():
          if v["age"]<=youngest_age:
             youngest_age=v["age"]
             youngest_id=k
       print("Oldest Patient Details")
       print("Patient ID :", youngest_id)
       print("Name       :", patient[youngest_id]["name"])
       print("Age        :", patient[youngest_id]["age"])
       print("Disease    :", patient[youngest_id]["disease"])
       print("Doctor     :", patient[youngest_id]["doctor"])
      case 10:
       print("Thankyou for visiting")

      case __:
       print("Invalid choice-------") 
 

           


