'''Assignment 1 – Employee Bonus System

Create a parent class Employee with the following attributes:

employee_id
employee_name
salary

Create two child classes:

Developer
Manager


Requirements

Take employee details from the user.
Use super() to initialize the common attributes.
Create a method calculate_bonus() in the parent class.
Override calculate_bonus() in both child classes.
Developer gets 10% of salary as bonus.
Manager gets 20% of salary as bonus.
Display employee details, bonus and total salary.
Sample Input
Enter Employee ID: 101
Enter Employee Name: Rahul
Enter Salary: 50000
Enter Employee Type: Developer

Expected Output
----- Employee Details -----
Employee ID   : 101
Employee Name : Rahul
Salary        : 50000
Employee Type : Developer
Bonus         : 5000
Total Amount  : 55000'''


class Employee:
    def __init__(self,employee_id,employee_name,salary):
        self.employee_id=employee_id
        self.employee_name=employee_name
        self.salary=salary

    def calculate_bonus(self):
        return 0


class Developer(Employee):
    def __init__(self,employee_id,employee_name,salary):
     super().__init__(employee_id,employee_name,salary)
    def calculate_bonus(self):
       return self.salary+0.10
    

class Manager(Employee):
     def __init__(self,employee_id,employee_name,salary):
       super().__init__(employee_id,employee_name,salary)
     def calculate_bonus(self):
            return self.salary+0.20
employee_id=int(input("Enter ID:"))
employee_name=input("Employee Name:")
salary=int(input("Employee Salary:"))
emp_type=input("Enployee Type:")
if emp_type=="Developer":
    emp=Developer(employee_id,employee_name,salary)
elif emp_type == "Manager":
    emp = Manager(employee_id, employee_name, salary)
bonus=emp.calculate_bonus()
print("----- Employee Details -----")
print("Employee ID   :", emp.employee_id)
print("Employee Name :", emp.employee_name)
print("Salary        :", emp.salary)
print("Employee Type :", emp_type)
print("Bonus         :", bonus)
print("Total Amount  :", emp.salary + bonus)


