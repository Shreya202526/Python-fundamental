'''Assignment 3: Student Marks Analysis

A student wants to calculate total marks, average, and percentage from 5 subjects.

Input:
Marks = 78, 85, 90, 88, 80

Expected Output:
Total = 421
Average = 84.2
Percentage = 84.2'''

sub1,sub2,sub3,sub4,sub5=map(int,input("Marks=").split(","))
total=sub1+sub2+sub3+sub4+sub5
avg=(sub1+sub2+sub3+sub4+sub5)/5
percentage=total/500*100
print(f"Total={total}\n Average={avg}\n Percentage={percentage}")
