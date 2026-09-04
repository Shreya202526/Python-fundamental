


students={}
print("=========================================")
print("STUDENT MANAGEMENT SYSTEM")
print("=========================================")

print("1. Add New Student")
print("2. Search Student")
print("3. Update Course")
print("4. Delete Student")
print("5. Display All Students")
print("6. Count Total Students")
print("7. Display Students By Course")
print("8. Display Students By City")
print("9. Find Student Paying Highest Fees")
print("10. Find Student Paying Lowest Fees")
print("11. Exit")
choice=int(input("Enter your choice:"))
match choice:
     case 1:
            n=int(input("Enter the number of Students: "))
            for i in range(n):
              id=int(input("Enter the Patient ID: "))
              Name=input("Enter the name of the patient:")
              Course=input("Enter the age of Patient:")
              Mobile=input("Enter the Gender:")
              Fees=int(input("Enter the Disease:"))
              City=input("Enter the doctor name")
              if id not in students:
               students[id]={
                 "name":Name,
                 "course":Course,
                 "mobile":Mobile,
                 "fees":Fees,
                 "city":City
                }
              print("Data Add successfully")

            else:
               print("Data Already Exists")
     case 2:
        id=int(input("Enter The Student id: "))
        if id in students:
           print("Student Id :", id)
           print("Name       :", students[id]["name"])
           print("Course      :", students[id]["course"])
           print("Mobile    :", students[id]["mobile"])
           print("Fees    :", students[id]["fees"])
           print("City    :", students[id]["city"])
        else:
            print("Student id not exists!!!")
     case 3:
        id=int(input("Enter the patient id: "))
        if id in students:
           new_course=input("Enter new disease:")
           students[id]["course"]=new_course
           print("Updated Successfully_____")
        else:
           print("Patient Id Not found")
     case 4:
         id=int(input("Enter the patient id"))     
         if id in students:
            del students[id]
            print(students)
            print("Student Record removed Successfully")
         else:
            print("Student id not found")
     case 5:
         for k,v in students.items():
                 print("---------------------------------")
                 print("Students ID :", k)
                 print("Name       :", v["name"])
                 print("Course      :", v["course"])
                 print("Fees     :", v["fees"])
     case 6:   
        print("Total students:",len(students)) 
     case 7:
           course = input("Enter course: ")
           found = False

           for k, v in students.items():
            if v["course"].lower() == course.lower():
              print(k, v["name"])
              found = True

           if found == False:
             print("No Student Found")

     case 8:
         city_id=None
         city=input("Enter city:")      
         for k,v in students.items():
            if v["city"]==city:
               print(k,v["name"])
     case 9:
        highest_fee=0
        highest=None       
        for k,v in students.items():
             if v["feess"]>=highest:
                 oldest_age=v["age"]
                 oldest_id=k
                 print("Oldest Patient Details")
                 print("Patient ID :", oldest_id)
                 print("Name       :", patient[oldest_id]["name"])
                 print("Age        :", patient[oldest_id]["age"])
                 print("Disease    :", patient[oldest_id]["disease"])
                 print("Doctor     :", patient[oldest_id]["doctor"])
               