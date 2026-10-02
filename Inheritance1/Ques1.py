'''============================================================
ASSIGNMENT 1 — EMPLOYEE MANAGEMENT SYSTEM
=========================================

SCENARIO:

A company wants to maintain information about different types of employees.

Create the following class hierarchy:

Employee
|
+-------- Developer
|
+-------- Manager

REQUIREMENTS:

1. Create a parent class Employee.

Employee should contain:

* employee_id
* employee_name
* salary

2. Create Developer and Manager classes that inherit from Employee.

3. Employee should have a method:

display_details()

4. Developer should have:

programming_language

and a method:

write_code()

5. Manager should have:

team_size

and a method:

manage_team()

6. The child-class constructors must initialize parent-class data using super().

7. Override display_details() in both child classes.

8. From the overridden method, call the parent display_details() using super().

9. salary must be encapsulated.

Implement:

@property
@salary.setter
@salary.deleter

10. Salary setter must reject salary <= 0.

11. Read ALL employee information from the user.

INPUT REQUIREMENT:

Ask the user:

Enter Employee ID:
Enter Employee Name:
Enter Salary:
Enter Employee Type:

1. Developer
2. Manager

If Developer:

Enter Programming Language:

If Manager:

Enter Team Size:

SAMPLE INPUT:

Enter Employee ID: 101
Enter Employee Name: Rahul
Enter Salary: 45000
Enter Employee Type: 1
Enter Programming Language: Python

EXPECTED OUTPUT:

## Employee Details

Employee ID: 101
Employee Name: Rahul
Salary: 45000
Role: Developer
Programming Language: Python

Rahul is developing applications using Python.

============================================================
'''




class Employee:
    def __init__(self,employee_id,employee_name,salary):
        self.employee_id=employee_id
        self.employee_name=employee_name
        self.__salary=salary
    @property
    def salary(self):
            return self.__salary
    @salary.setter
    def salary(self,n):
            if n<=0:
                raise ValueError("salary must be greater than zer0")
            else:
                self.__salary=n
    @salary.deleter
    def salary(self):
            print("Deleting salary")
            del self.__salary

    def display_details(self):
        
            print(self.employee_id)
            print(self.employee_name)
            print(self.salary)
class Developer(Employee):
    def __init__(self,employee_id,employee_name,salary,programming_lang):
        super().__init__(employee_id,employee_name,salary)
        self.programming_lang=programming_lang

    def display_details(self):
        super().display_details()
        print(self.employee_id)
        print(self.employee_name)
        print(self.salary)
        print(self.programming_lang)

    def write_code(self):
        print("write code")
class Manager(Employee):
    def __init__(self,employee_id,employee_name,salary,team_size):
        super().__init__(employee_id,employee_name,salary)
        self.team_size=team_size
    def display_details(self):
        #super().display_details()
        print(self.employee_id)
        print(self.employee_name)
        print(self.salary)
        print(self.team_size)

    def manage_team(self):
        print("manage team")


employee_id=int(input("Enter the employee Id:"))
employee_name=input("Enter the Employee Name:")
salary=int(input("Enter the salary"))
type=input("Enter the employee type Developer/Manager:")
if type=="Developer":
    programming_lang=input("Enter Programming language:")
    employee=Developer(employee_id,employee_name,salary,programming_lang)
    employee.display_details()
    employee.write_code()

elif type=="Manager":
    team_size=input("Enter the team size:")
    employee=Manager(employee_id,employee_name,salary,team_size)
    employee.display_details()
    employee.manage_team()

else:
    print("Invalid ")
