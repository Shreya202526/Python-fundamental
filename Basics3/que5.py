
'''Assignment 5: Salary Breakdown

An employee wants to calculate salary per day and per hour.

Input:
Monthly salary = 36000
Working days = 24
Working hours per day = 8

Expected Output:
Salary per day = 1500.0
Salary per hour = 187.5'''



monthly_salary=int(input("Monthly salary="))
working_days=int(input("Working days="))
working_hrs=int(input("Working hours per day="))
salary_per_day=monthly_salary//working_days
salary_per_hrs=salary_per_day/working_hrs
print(f"Salary per day= {salary_per_day}\n Salary per hour={salary_per_hrs}")
