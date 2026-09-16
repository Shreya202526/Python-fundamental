'''2.
 Employee Joining & Experience System

Create an employee experience calculator.

Read:

Employee name
Joining date
Current date

Calculate:

Total days worked
Total years worked
Total months approximately
Experience in Years Months Days
Whether employee has completed 1 year
Whether employee has completed 5 years

Example:

Enter employee name: Rahul
Enter joining date: 10-06-2021
Enter current date: 10-09-2026

Output:

Employee: Rahul
Joining Date: 10-06-2021
Experience: 5 Years 3 Months 0 Days
Total Days Worked: 1918
5 Years Completed: Yes'''

from datetime import date,datetime
name=input("Enter Employee name: ")
joining=input("Enter joining date: ")
current_date=input("Enter the current date: ")

new_joining=datetime.strptime(joining,"%d-%m-%Y").date()
current_date=datetime.strptime(current_date,"%d-%m-%Y").date()
print(f"Employee:{name}")
print(f"joining Date {new_joining}")
total_days=(current_date-new_joining).days
print("Total Days Worked:",total_days)
working_year=current_date.year-new_joining.year

if (current_date.month, current_date.day) < (new_joining.month, new_joining.day):
  working_year -= 1 
  print("Total Years Worked:", working_year)
  if working_year >= 5:
    print("5 years completed: Yes") 
  else:
    print("5 years completed: No")
working_month=current_date.month-new_joining.month

if (current_date.month, current_date.day) < (new_joining.month, new_joining.day):
  working_month -= 1 
  print("Total Years Worked:", working_year)
working_day=current_date.day-new_joining.day

if (current_date.month, current_date.day) < (new_joining.month, new_joining.day):
  working_day -= 1 
  print("Total Years Worked:", working_year)
print(f"{working_year} years {working_month} Month { working_day} days")


