'''Question 4: Student Result Processing System
Scenario

A college wants to automate result generation by calculating total marks, percentage, and grade.

Requirements

Create a class named Student with:

roll_number
student_name
marks1
marks2
marks3

Initialize the values using a constructor.

Calculations
Total = Marks1 + Marks2 + Marks3
Percentage = Total / 3
Grade Criteria
Percentage Grade
90 and above A
75 to 89 B
60 to 74 C
Below 60 D
Sample Input
Enter Roll Number : 101
Enter Student Name : Priya Sharma
Enter Marks in Subject 1 : 85
Enter Marks in Subject 2 : 90
Enter Marks in Subject 3 : 88
Sample Output
------ Student Result ------
Roll Number      : 101
Student Name     : Priya Sharma
Total Marks      : 263
Percentage       : 87.67
Grade            : B'''


class Student:
    def __init__(self,roll_number,student_name,marks1,marks2,marks3):
        self.roll_number=roll_number
        self.student_name=student_name
        self.marks1=marks1
        self.marks2=marks2
        self.marks3=marks3

    def calculate_Total(self):
        self.total=self.marks1+self.marks2+self.marks3

    def calculate_percentage(self):
        self.percentage=self.total/3

    def calculate_grade(self):
        if self.percentage>=90:
             self.grade="A"
        elif 75<=self.percentage<=89:
            self.grade="B"
        elif 60<=self.percentage<=74:
            self.grade="C"
        else:
            self.grade="D"


    def display_details(self):
        print("Roll Number  :",self.roll_number)
        print("Student Name :",self.student_name)
        print("Total Marks  :",self.total)
        print("Percentage   :",self.percentage)
        print("Grade        :",self.grade)

roll_number=int(input("Enter Roll Number:"))
student_name=input("Enter Student Name:")
marks1=int(input("Enter marks in subject1:"))
marks2=int(input("Enter marks in subject2:"))
marks3=int(input("Enter marks in subject3:"))

s1=Student(roll_number,student_name,marks1,marks2,marks3)
s1.calculate_Total()
s1.calculate_percentage()
s1.calculate_grade()
s1.display_details()