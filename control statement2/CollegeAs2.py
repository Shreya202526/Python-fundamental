
'''2. College Result Processing System


A college wants to generate grades for students automatically based on their marks in an exam. The grading criteria are as follows:

* 90 and above → Grade A
* 75 to 89 → Grade B
* 60 to 74 → Grade C
* 50 to 59 → Grade D
* Below 50 → Fail

Write a Python program to display the grade of a student.

Input:
Enter marks: 67

Output:
Grade: C'''
   

percentage=int(input("Enter marks:"))
if percentage>=90:
   print("Grade A")
elif percentage>=75 and percentage<=89:
   print("Grade B")
elif percentage>=60 and percentage<=74:
   print("Grade C")
elif percentage>=50 and percentage<=59:
   print("Grade D")
elif percentage<=50:
   print("fail")
