'''1.
STUDENT RESULT MANAGEMENT SYSTEM

Scenario:

A college examination department wants to automate the process of generating student results. 
The staff should be able to
enter student details, calculate marks, determine grades, and display a complete report 
card using a menu-driven application.

Develop a Python program using multiple user-defined functions and a menu-driven approach 
to perform the following operations.

MENU

1. Add Student Details
2. Calculate Total Marks
3. Calculate Percentage
4. Find Grade
5. Display Complete Result
6. Find Highest Subject Mark
7. Find Lowest Subject Mark
8. Exit

Functional Requirements

1. Add Student Details

   * Student Name
   * Roll Number
   * Marks of 5 Subjects

2. Calculate Total Marks

3. Calculate Percentage

4. Find Grade

5. Display Complete Result

6. Find Highest Subject Mark

7. Find Lowest Subject Mark

8. Exit

Grade Criteria

Percentage        Grade

90 - 100          A+
80 - 89           A
70 - 79           B
60 - 69           C
50 - 59           D
Below 50          Fail

Constraints

* Marks should be between 0 and 100.
* Display an appropriate message for invalid marks.
* The program should continue until the user chooses Exit.

Sample Input / Output

******** STUDENT RESULT MANAGEMENT ********

1. Add Student Details
2. Calculate Total Marks
3. Calculate Percentage
4. Find Grade
5. Display Result
6. Find Highest Mark
7. Find Lowest Mark
8. Exit

Enter Choice : 1

Enter Student Name : Ajay
Enter Roll Number : 101

Enter Mark 1 : 78
Enter Mark 2 : 85
Enter Mark 3 : 92
Enter Mark 4 : 88
Enter Mark 5 : 77

Student details added successfully.

Enter Choice : 2

Total Marks = 420

Enter Choice : 3

Percentage = 84.0

Enter Choice : 4

Grade = A

Enter Choice : 6

Highest Mark = 92

Enter Choice : 7

Lowest Mark = 77

Enter Choice : 5

----------- RESULT CARD -----------

Name        : Ajay
Roll Number : 101

Marks
Subject 1 : 78
Subject 2 : 85
Subject 3 : 92
Subject 4 : 88
Subject 5 : 77

Total Marks : 420
Percentage  : 84.0
Grade       : A
Highest Mark: 92
Lowest Mark : 77

Enter Choice : 8

Thank You. Program Terminated.

Important Instructions

1. The solution must be developed using multiple user-defined functions.
2. Use appropriate parameters wherever data needs to be passed between functions.
3. Use return statements wherever a function needs to send a result back to the caller.
4. Avoid using unnecessary global variables.
5. Implement the application using a menu-driven approach.
6. Perform proper input validation.
7. Write meaningful function names and maintain proper code readability.

'''
Student=[]
def add(name,rollno,subject1,subject2,subject3,subject4,subject5):
       student={
          "name":name,
          "rollno":rollno,
          "marks":[subject1,subject2,subject3,subject4,subject5]
       }
       Student.append(student)
       return Student

def total():
    total=0
    for x in Student[0]["marks"]:
       total+=x
    return total
    
def percentage():
    t=total()
    percent=(t/500)*100
    return percent
def grade():
    p=percentage()
    if p>=90:
         return "A+"
    elif p>=80 :
         return "A"
    elif p>=70 :
        return  "B"
    elif p>=60:
         return  "C"
    elif p>=50 :
        return  "D"
    else:
        return "Fail"


def highest():
    highest=0
    for x in Student[0]["marks"]:
        if x>highest:
            highest=x
    return highest
def lowest():
    lowest=total()
    for x in Student[0]["marks"]:
         if x<lowest:
               lowest=x
    return lowest
def display():
    print("Name          :", Student[0]["name"])
    print("Roll Number   :", Student[0]["rollno"])

    print("\nMarks")
    print("Subject 1     :", Student[0]["marks"][0])
    print("Subject 2     :", Student[0]["marks"][1])
    print("Subject 3     :", Student[0]["marks"][2])
    print("Subject 4     :", Student[0]["marks"][3])
    print("Subject 5     :", Student[0]["marks"][4])
    print("Total Marks   :", total())
    print("Percentage    :", percentage())
    print("Grade         :", grade())
    print("Highest Mark  :", max(Student[0]["marks"]))
    print("Lowest Mark   :", min(Student[0]["marks"]))
while True:
   print("Menu")
   print("1.Add Student Details")
   print("2.Calculate Total Marks")
   print("3.Calculate Percentage")
   print("4 Find Grade")
   print("5.Display Complete Result")
   print("6.Find Highest Subject Mark")
   print("7.Find Lowest Subject Mark")
   print("8.Exit")
   choice=int(input("Enter your choice:"))
   match choice:
      case 1:
         name=input("Enter the name of the student: ")
         roll_no=input("Enter the roll_no of student:")
         sub1=int(input("Enter the marks of subject1: "))
         sub2=int(input("Enter the marks of subject2: "))
         sub3=int(input("Enter the marks of subject3: "))
         sub4=int(input("Enter the marks of subject4: "))
         sub5=int(input("Enter the marks of subject5: "))
         print(add(name,roll_no,sub1,sub2,sub3,sub4,sub5))
         print("Details Add Successfully-----")
      case 2:
         print("Total marks:",total())
      case 3:
           print("percentage:",percentage())
      case 4:
           print("Grade:",grade())
      case 5:
           print("------Resultcard-------")
           print(display())
      case 6:
           print("Highest Marks:",highest())
      case 7:
           print("Lowest Marks:",lowest())
      case 8:
           print("Thankyou  program terminated")
      case __:
           print("Invalid choice")