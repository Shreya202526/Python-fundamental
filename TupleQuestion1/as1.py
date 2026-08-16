'''=====================================================================
QUESTION 1: EMPLOYEE SALARY ANALYSIS
====================================

A company wants to store employee details and generate salary reports using NamedTuple.

Fields:
emp_id, emp_name, department, salary

Requirements:

1. Read N employee details from the user and store them in a list of NamedTuples.

---

2. Display all employee details.

---

3. Find and display the employee with the highest salary.

---

4. Find and display the employee with the lowest salary.

---

5. Calculate and display the average salary of all employees.

---
6. Accept a department name from the user and display all employees belonging to that department.

---

Test Case:

Input:
Enter number of employees: 4

101 Rahul IT 50000
102 Priya HR 45000
103 Amit IT 70000
104 Neha Finance 60000

Enter department: IT

Expected Output:
Highest Salary Employee:
103 Amit IT 70000

Lowest Salary Employee:
102 Priya HR 45000

Average Salary:
56250.0

Employees in IT Department:
101 Rahul IT 50000
103 Amit IT 70000

'''

from collections import namedtuple
Employee=namedtuple("emp",["emp_id","emp_name","department","salary"])
n=int(input("Enter the number of Employee"))

employee=[]

for i in range(n):
    print("Details")
    id=int(input("Enter the id="))
    name=input("Enter the name=")
    dept=input("Enter the department=")
    sal = int(input("Enter the Salary="))
    emp = Employee(id,name,dept,sal)
    employee.append(emp)

print(employee)
for x in employee:
    print(x.emp_id,x.emp_name,x.department,x.salary)

dept=input("Enter the deparment=")
max_salary=None
avg=0
sum=0
min_salary=None
for x in employee:
    sum+=x.salary
    if max_salary is None or x.salary > max_salary:
         max_salary = x.salary

    if min_salary is None or x.salary < min_salary:
         min_salary = x.salary
Avg=sum/n 
if max_salary is not None:
    print("Highest salary Employee:", max_salary)
    print(x.emp_id,x.emp_name,x.department,x.salary)

    print("Lowest salary Employee:", min_salary)
    print(x.emp_id,x.emp_name,x.department,x.salary)
else:
    print("Department not found")
print("Average Salary=",Avg) 
for x in employee:
    if x.department == dept:
        print(f"Employee in{dept}{x.emp_id} {x.emp_name} {x.department} {x.salary}")
