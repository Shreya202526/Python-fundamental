'''Assignment 4 – Menu-Driven Future Date Calculator

Develop a menu-driven Python program using the datetime module to calculate a future date.

The program should allow the user to add days, weeks, hours, or minutes to a given date/time.

Use timedelta for all date and time calculations.

Menu
========== FUTURE DATE CALCULATOR ==========

1. Add Days
2. Add Weeks
3. Add Hours
4. Add Minutes
5. Exit

Enter your choice:
Case 1 – Add Days

Read:

Starting date
Number of days
Input
Enter your choice: 1

Enter starting date (DD-MM-YYYY): 10-09-2026
Enter number of days to add: 100
Output
Starting Date : 10-09-2026
Days Added    : 100
Future Date   : 19-12-2026
Case 2 – Add Weeks

Read:

Starting date
Number of weeks
Input
Enter your choice: 2

Enter starting date (DD-MM-YYYY): 10-09-2026
Enter number of weeks to add: 4
Output
Starting Date : 10-09-2026
Weeks Added   : 4
Future Date   : 08-10-2026
Case 3 – Add Hours

For this case, the student should take date and time as input.

Input
Enter your choice: 3

Enter date and time (DD-MM-YYYY HH:MM): 10-09-2026 10:30
Enter number of hours to add: 15
Output
Starting Date & Time : 10-09-2026 10:30
Hours Added          : 15
Future Date & Time   : 11-09-2026 01:30

This case should test whether students understand that adding hours can change the date.

Case 4 – Add Minutes

Take date/time and number of minutes.

Input
Enter your choice: 4

Enter date and time (DD-MM-YYYY HH:MM): 10-09-2026 23:30
Enter number of minutes to add: 90
Output
Starting Date & Time : 10-09-2026 23:30
Minutes Added        : 90
Future Date & Time   : 11-09-2026 01:00

Students must correctly handle the change from 10 September → 11 September.

Case 5 – Exit
Enter your choice: 5

Thank you for using Future Date Calculator!
Complete Sample Run
========== FUTURE DATE CALCULATOR ==========

1. Add Days
2. Add Weeks
3. Add Hours
4. Add Minutes
5. Exit

Enter your choice: 1

Enter starting date (DD-MM-YYYY): 25-12-2026
Enter number of days to add: 15

Starting Date : 25-12-2026
Days Added    : 15
Future Date   : 09-01-2027


========== FUTURE DATE CALCULATOR ==========

1. Add Days
2. Add Weeks
3. Add Hours
4. Add Minutes
5. Exit

Enter your choice: 4

Enter date and time (DD-MM-YYYY HH:MM): 31-12-2026 23:30
Enter number of minutes to add: 90

Starting Date & Time : 31-12-2026 23:30
Minutes Added        : 90
Future Date & Time   : 01-01-2027 01:00


========== FUTURE DATE CALCULATOR ==========

1. Add Days
2. Add Weeks
3. Add Hours
4. Add Minutes
5. Exit

Enter your choice: 5

Thank you for using Future Date Calculator!'''



from datetime import datetime,timedelta
while True:

   print("Menu")
   print("========== FUTURE DATE CALCULATOR ==========")

   print("1. Add Days")
   print("2. Add Weeks")
   print("3. Add Hours")
   print("4. Add Minutes")
   print("5. Exit")
   choice=int(input("Enter your choice: "))
   match choice:
      case 1:
         d=input("Enter starting date (DD-MM-YYYY): ")
         day=int(input("Enter number of days to add:"))
         d1=datetime.strptime(d,"%d-%m-%Y").date()
         next_date=d1+timedelta(days=day)
         print(f"Starting Date :{d1}")
         print(f"Days Added    : {day}")
         print(f"Future Date   : {next_date}")
      case 2:
         d=input("Enter starting date (DD-MM-YYYY): ")
         week=int(input("Enter number of weeks to add:"))
         d1=datetime.strptime(d,"%d-%m-%Y").date()
         next_date=d1+timedelta(weeks=week)
         print(f"Starting Date :{d1}")
         print(f"Weeks Added    : {week}")
         print(f"Future Date   : {next_date}")
      case 3:
         d=input("Enter starting date (DD-MM-YYYY): ")
         hour=int(input("Enter number of hour to add:"))
         d1=datetime.strptime(d,"%d-%m-%Y %H:%M")
         next_date=d1+timedelta(hours=hour)
         print(f"Starting Date :{d1}")
         print(f"hours Added    : {hour}")
         print(f"Future Date   : {next_date}")
      case 4:
         d=input("Enter starting date (DD-MM-YYYY): ")
         minutes=int(input("Enter number of minutes to add:"))
         d1=datetime.strptime(d,"%d-%m-%Y %H:%M")
         next_date=d1+timedelta(minutes=minutes)
         print(f"Starting Date :{d1}")
         print(f"Minute  Added    : {minutes}")
         print(f"Future Date   : {next_date}")
      case 5:     
         print("Exits======") 
      case __:
         print("You entered wrong choice")        