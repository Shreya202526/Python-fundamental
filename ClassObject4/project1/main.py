from model.student import Student








students=[]
n=int(input("Enter the number of student:"))
for i in range(n):
   roll_no=int(input("Enter the roll_no:"))
   name=input("Enter the name of student:")
   marks=int(input("Enter the marks of the student:"))
   s1=Student(roll_no,name,marks)
   students.append(s1)
def display_students(students):
    print("\n------ ALL STUDENT DETAILS ---------")

    for student in students:
        print(student.roll_no,student.name,student.marks)
    return student

def display_60_above(students):
    print("-----students having marks greater than 60:---")
    for student in students:
          if student.marks > 60:
              print(student.roll_no,student.name,student.marks)


def display_highest(students):
    highest=0
    highest_student=None
    print("-----Highest marks-----")
    for student in students:
          if student.marks>highest:
              highest=student.marks
              highest_student=student
    print(highest_student.roll_no,highest_student.name,highest_student.marks)

def display_average(students):
    print("----Average Marks-------")
    sum=0
    for student in students:
            sum+=student.marks
    avg=sum/n
    print(avg)
        


display_students(students)
display_60_above(students)
display_highest(students)
display_average(students)


