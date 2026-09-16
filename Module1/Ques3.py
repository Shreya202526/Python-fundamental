'''Assignment 3 — Date Difference Calculator

Create a program that accepts two dates and displays:

Enter first date: 10-09-2026
Enter second date: 25-12-2026

Display:

Difference in days
Difference in weeks
Difference in hours
Difference in minutes

Example:

Days Difference: 106
Weeks Difference: 15
Hours Difference: 2544
Minutes Difference: 152640
'''

from datetime import date,datetime
first_date=input("Enter first date: ")
second_date=input("Enter Second date: ")

first_date1=datetime.strptime(first_date,"%d-%m-%Y").date()
second_date1=datetime.strptime(second_date,"%d-%m-%Y").date()

print(first_date1)
print(second_date1)
day_difference=second_date1-first_date1
print("Days Difference :",day_difference.days)

week_difference=(day_difference.days/7)
print("Weak Difference:",week_difference)

Hour_differnce=(day_difference.days*24)
print("Hour Difference",Hour_differnce)


Minute_differnce=(day_difference.days*24*60)
print("Minute Difference",Minute_differnce)
