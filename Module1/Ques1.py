'''Assignment 1 — Age Calculator

Create a program that accepts the user's date of birth and calculates:

Current age in years
Completed months
Total number of days lived
Next birthday date
Number of days remaining for the next birthday

Input:

Enter DOB (DD-MM-YYYY): 15-08-1998

Expected Output:

Age: 28 years
Total Days Lived: XXXXX days
Next Birthday: 15-08-2027
Days Remaining: XX days'''


from datetime import datetime,timedelta
DOB=input("Enter DOB(DD-MM-YYYY):")
bdate=datetime.strptime(DOB,"%d-%m-%Y")
today=datetime.now()
#print(bdate)
#print(today)
age=today.year-bdate.year
print(f"Age {age} years")
total_days=(today-bdate).days
print(f"Total Days:{total_days}")
next_bday = datetime(today.year, bdate.month, bdate.day)
if next_bday <= today:
    next_bday = datetime(today.year + 1, bdate.month, bdate.day)
print(next_bday)
next_bday_after=(next_bday-today).days
print("Days Remaining",next_bday_after)