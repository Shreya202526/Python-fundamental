'''2.
=========================================
ONLINE COURSE ENROLLMENT SYSTEM
=========================================

An institute offers:
1. Python Course
2. Java Course

Store enrolled student email IDs using sets.

Menu:
1. Enroll Student in Python
2. Enroll Student in Java
3. Display Python Students
4. Display Java Students
5. Find Students Enrolled in Both Courses
6. Find Students Enrolled Only in Python
7. Find Students Enrolled Only in Java
8. Check Enrollment in Python Course
9. Display Total Unique Students
10. Exit

Requirements:
- Use two sets.
- Use membership operator (in).
- Use union, intersection and difference operations.'''



python_course=set()
java_course=set()
while True:
   
  print("Menu:")
  print("1.Enroll Student in Python ")
  print("2.Enroll Student in Java ")
  print("3. Display Python Students")
  print("4. Display Java Students")
  print("5. Find Students Enrolled in Both Courses")
  print("6. Find Students Enrolled Only in Python")
  print("7. Find Students Enrolled Only in Java")
  print("8. Check Enrollment in Python Course")
  print("9. Display Total Unique Students")
  print("10. Exit")

  choice=int(input("Enter your choice="))

  match choice:
      case 1:
           n=int(input("Enter the number of students you want to add:"))
           for i in range(1,n+1):
            student=input(f"Enter the name of the student {i}: ")
            python_course.add(student)
           print("Students Added to the python course")

      case 2:
           n=int(input("Enter the number of students you want to add:"))
           for i in range(1,n+1):
            student=input(f"Enter the name of the student {i}: ")
            java_course.add(student)
           print("Students Added to the java course")

      case 3:
         if python_course:
           print(python_course)
         else:
          print("No Student in python course")

      case 4:
         if java_course:
          print(java_course)
         else:
          print("No Student in java course")
      case 5:
         if python_course and java_course:
            both=python_course.intersection(java_course)
            print(both)
         else:
            print("Firstly add student in both club")   


      case 6:
        if python_course:
          only_python=python_course.difference(java_course)
          print(only_python)
        else:
          print("No Member in Coding club")

      case 7:
        if java_course:
          only_java=python_course.difference(java_course)
          print(only_java)
        else:
          print("No Member in Robotics club")


      case 8:
        if python_course and java_course:
          All_unique=python_course.union(java_course)
          print(All_unique)
        else:
          print("firstly add member in both club")

      case 9:
        if python_course and java_course:
          total_memebers=len(python_course.union(java_course))
          print(total_memebers)
        else:
          print("firstly add member in both club")
      case 10:
        print("Exitingggg......")
      case __ :
        print("you enter invalid choice")
   
