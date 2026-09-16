'''ASSIGNMENT 5 – MENU-DRIVEN PAST DATE & TIME CALCULATOR


Create a menu-driven Python program that allows the user to calculate a date/time in the past by subtracting days, weeks, hours, or minutes.

Menu
========== PAST DATE & TIME CALCULATOR ==========

1. Subtract Days
2. Subtract Weeks
3. Subtract Hours
4. Subtract Minutes
5. Exit

Enter your choice:
CASE 1 – Subtract Days
Input
Enter your choice: 1

Enter starting date (DD-MM-YYYY): 10-09-2026
Enter number of days to subtract: 100
Output
Starting Date : 10-09-2026
Days Subtracted : 100
Past Date : 02-06-2026
CASE 2 – Subtract Weeks
Input
Enter your choice: 2

Enter starting date (DD-MM-YYYY): 10-09-2026
Enter number of weeks to subtract: 6
Output
Starting Date : 10-09-2026
Weeks Subtracted : 6
Past Date : 30-07-2026
CASE 3 – Subtract Hours

Here the student must read both date and time.

Input
Enter your choice: 3

Enter date and time (DD-MM-YYYY HH:MM): 10-09-2026 10:30
Enter number of hours to subtract: 15
Output
Starting Date & Time : 10-09-2026 10:30
Hours Subtracted     : 15
Past Date & Time     : 09-09-2026 19:30
CASE 4 – Subtract Minutes
Input
Enter your choice: 4

Enter date and time (DD-MM-YYYY HH:MM): 10-09-2026 01:00
Enter number of minutes to subtract: 90
Output
Starting Date & Time : 10-09-2026 01:00
Minutes Subtracted   : 90
Past Date & Time     : 09-09-2026 23:30
CASE 5 – Exit
Enter your choice: 5

Thank you for using Past Date & Time Calculator!'''


from datetime import datetime,timedelta
while True:

   print("Menu")
   print("========== FUTURE DATE CALCULATOR ==========")

   print("1. Subtract Days")
   print("2. Subtract Weeks")
   print("3. Subtract Hours")
   print("4. Subtract Minutes")
   print("5. Exit")
   choice=int(input("Enter your choice: "))
   match choice:
      case 1:
         d=input("Enter starting date (DD-MM-YYYY): ")
         day=int(input("Enter number of days to add:"))
         d1=datetime.strptime(d,"%d-%m-%Y").date()
         next_date=d1-timedelta(days=day)
         print(f"Starting Date :{d1}")
         print(f"Days Subtracted    : {day}")
         print(f"Future Date   : {next_date}")
      case 2:
         d=input("Enter starting date (DD-MM-YYYY): ")
         week=int(input("Enter number of weeks to add:"))
         d1=datetime.strptime(d,"%d-%m-%Y").date()
         next_date=d1-timedelta(weeks=week)
         print(f"Starting Date :{d1}")
         print(f"Weeks Subtracted    : {week}")
         print(f"Future Date   : {next_date}")
      case 3:
         d=input("Enter starting date (DD-MM-YYYY): ")
         hour=int(input("Enter number of hour to add:"))
         d1=datetime.strptime(d,"%d-%m-%Y %H:%M")
         next_date=d1-timedelta(hours=hour)
         print(f"Starting Date :{d1}")
         print(f"hours subtracted   : {hour}")
         print(f"Future Date   : {next_date}")
      case 4:
         d=input("Enter starting date (DD-MM-YYYY): ")
         minutes=int(input("Enter number of minutes to add:"))
         d1=datetime.strptime(d,"%d-%m-%Y %H:%M")
         next_date=d1-timedelta(minutes=minutes)
         print(f"Starting Date :{d1}")
         print(f"Minute  Subtracted   : {minutes}")
         print(f"Future Date   : {next_date}")
      case 5:     
         print("Exits======") 
      case __:
         print("You entered wrong choice")        