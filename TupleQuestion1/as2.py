'''=====================================================================
QUESTION 2: STUDENT RESULT PROCESSING
=====================================

A training institute wants to manage student records using NamedTuple.

Fields:
roll_no, name, course, marks

Requirements:

1. Read N student records from the user and store them in a list of NamedTuples.

---

2. Display all student details.

---

3. Find and display the topper of the class.

---

4. Count and display the number of students scoring above 80 marks.

---

5. Calculate and display the average marks.

---

6. Accept a course name from the user and display all students enrolled in that course.

---

Test Case:

Input:
Enter number of students: 4

1 Ravi Python 85
2 Anjali Java 78
3 Karan Python 92
4 Pooja Testing 88

Enter course: Python

Expected Output:
Topper:
3 Karan Python 92

Students Above 80:
3

Average Marks:
85.75

Students in Python Course:
1 Ravi Python 85
3 Karan Python 92'''


from collections import namedtuple
Result=namedtuple("res",["roll_no","name","course","marks"])
n=int(input("Enter the number of students"))
result=[]
for i in range(n):
    print("Details")
    rollno=int(input("Enter the rollno="))
    name=input("Enter the name=")
    course=input("Enter the course=")
    marks = int(input("Enter the marks="))
    r= Result(rollno,name,course,marks)
    result.append(r)
print(result)
for x in result:
    print(x.roll_no,x.name,x.course,x.marks)
course=input("Enter the course:")
max_marks=None
count=0
Avg=0
sums=0
for x in result:
    sums+=x.marks
    if max_marks==None or x.marks>=max_marks:
        max_marks=x.marks
    if x.marks>=80:
        count+=1
Avg=sums/n
print("Topper:")
print(x.roll_no,x.name,x.course,x.marks)

print("Student above 80:")
print(count)

print("Average Marks:",Avg)
for x in result:
 if x.course==course:
    print(x.roll_no,x.name,x.course,x.marks)

    
