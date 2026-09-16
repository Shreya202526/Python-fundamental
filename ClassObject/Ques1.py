'''Assignment 1: Student Result Calculator

 A school wants to calculate the total marks and percentage of a student.

Create a class Student with the following attributes:

Student name

Roll number

Marks in English

Marks in Mathematics

Marks in Science

Create the following methods:

calculate_total() – Calculate the total marks.

calculate_percentage() – Calculate the percentage.

display_result() – Display student details, total, and percentage.

Expected output:

Student Name: Ajay
Roll Number: 101
Total Marks: 240
Percentage: 80.0%'''

class Student:
    def set(self,name,roll_no,english,mathematics,science):
        self.name=name
        self.roll_no=roll_no
        self.english=english
        self.mathematics=mathematics
        self.science=science

    def calculate_total(self):
        self.total=self.english+self.mathematics+self.science

    def calculate_percentage(self):
        self.percentage = (self.total / 300) * 100

    def display_result(self):
        print()
        print("Student Name:",self.name)
        print("Roll Number:",self.roll_no)
        print("Total Marks:",self.total)
        print("Percentage:",self.percentage,"%")
        
s1=Student()
s1.set("Shreya",101,90,80,70)
s1.calculate_total()
s1.calculate_percentage()
s1.display_result()