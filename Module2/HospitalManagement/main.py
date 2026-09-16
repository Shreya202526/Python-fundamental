


from patient.patient_module import add_patient, display_patients, search_patient
from doctor.doctor_module import display_doctors,add_doctor
from appointment.appoitment_module import book_appointment,show_appointments
from billing.billing_module import generate_bill
while True:
 print("Menu:")

 print("========== Hospital Management System ==========")

 print("1. Add Patient")

 print("2. Display Patients")

 print("3. Search Patient")

 print("4. Add Doctor")

 print("5. Display Doctors")

 print("6. Book Appointment")

 print("7. Show Appointments")

 print("8. Generate Bill")

 print("9. Exit")
 choice=int(input("Enter your Choice: "))
 match choice:
    case 1:
        add_patient()
    case 2:
       display_patients()
    case 3:
       search_patient()
    case 4:
       add_doctor()
    case 5:
       display_doctors()
    case 6:
       book_appointment()
    case 7:
       show_appointments()
    case 8:
       generate_bill()
    case 9:
       print("Thankyou for visiting====")
    case __:
       print("Invalid choice")