'''Assignment 2: Employee Salary Calculator

A company wants to calculate an employee's gross salary.

Create a class Employee with the following attributes:

Employee ID

Employee name

Basic salary

HRA percentage

DA percentage

Create the following methods:

calculate_hra() – Calculate HRA.

calculate_da() – Calculate DA.

calculate_gross_salary() – Calculate gross salary.

display_salary() – Display employee salary details.

Formula:

HRA = Basic Salary × HRA Percentage / 100
DA = Basic Salary × DA Percentage / 100
Gross Salary = Basic Salary + HRA + DA'''


class Employee:
    def set(self,id,name,salary,hra,da):
        self.id=id
        self.name=name
        self.salary=salary
        self.hra=hra
        self.da=da

    def calculate_hra(self):
        self.HRA=self.salary*(self.hra/100)

    def calculate_da(self):
        self.DA=self.salary*(self.da/100)

    def calculate_gross_salary(self):
        self.gross=self.salary+self.HRA+self.DA

    def display_salary(self):
        print("Employee ID:",self.id)
        print("Employee Name:",self.name)
        print("HRA:",self.HRA)
        print("DA",self.DA)
        print("Gross Salary:",self.gross)

e1=Employee()
e1.set(101,"Shreya",70000,5,6)
e1.calculate_hra()
e1.calculate_da()
e1.calculate_gross_salary()
e1.display_salary()

