from model.employee import Employee


n=int(input("Enter the number of employee:"))
employees=[]
for i in range(n):

  employee_id=int(input("Enter the employee Id:"))
  name=input("Enter the name:")
  salary=int(input("Enter the salary :"))
  department=input("Enter the deparment:")
  e1=Employee(employee_id,name,salary,department)
  employees.append(e1)

def display_employees(employees):
    print("\nALL EMPLOYEES DETAILS:")

    for employee in employees:
        print(employee.employee_id,employee.name,employee.salawwry,employee.department)
    return employee

display_employees(employees)

def display_above_salary(employees):
    print("Employees with salary greater than 40000:")
    for employee in employees:
          if employee.salary > 40000:
              print(employee.employee_id,employee.name,employee.salary,employee.department)
display_above_salary(employees)

def  display_itemployee(employees):
       for employee in employees:
              if employee.department=="IT":
                  print(employee.employee_id,employee.name,employee.salary,employee.department)
display_itemployee(employees)



def display_highest(employees):
    highest=0
    highest_employee=None
    print("Highest Salary:")
    for employee in employees:
          if employee.salary>highest:
              highest=employee.salary
              highest_employee=employee
    print(highest_employee.employee_id,highest_employee.name,highest_employee.salary,highest_employee.department)



def display_average(employees):
    print("Total salary:")
    sum=0
    for employee in employees:
            sum+=employee.salary
    avg=sum/n
    print(sum)
    print("Average salary:")
    print(avg)
display_average(employees)