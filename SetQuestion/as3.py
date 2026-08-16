'''.
=========================================
WEBSITE VISITOR TRACKING SYSTEM
=========================================

A website stores unique visitor IDs.

Menu:
1. Add Visitor
2. Remove Visitor
3. Check Visitor
4. Display All Visitors
5. Count Unique Visitors
6. Clear Visitor Data
7. Exit

Requirements:
- Use a set to store visitor IDs.
- Duplicate visitor IDs should not be stored.
- Use add(), remove(), and membership operation'''



visitor=set()


while True:
   print("Menu:")
   print("1. Add Visitor")
   print("2. Remove Visitor")
   print("3. Check Visitor")
   print("4. Display All Visitors")
   print("5. Count Unique Visitors")
   print("6. Clear Visitor Data")
   print("7. Exit")
   choice=int(input("Enter your choice:"))
   match choice:
       case 1:
           n=int(input("Enter the number of students you want to add:"))
           for i in range(1,n+1):
            student=input(f"Enter the name of the student {i}: ")
            visitor.add(student)
            print("Students Added to the Coding clud")
       case 2:
           n=int(input("Enter the number of students you want to add:"))
           for i in range(1,n+1):
            student=input(f"Enter the name of the student {i}: ")
            visitor.remove(student)
            print("Students Removed to the Coding clud")
       case 3:
            visitor_name=input("Enter the visitor name you want to check")
            if visitor_name in visitor:
               print("Visitor Found")
            else:
               print("visitor not found")
       case 4:
            if visitor:
               print("All Visitors",visitor)
            else:
               print("No Visitor")

       case 5:
          if visitor:
             print("Total number of unique visitor",len(visitor))
          else:
             print("No visitor")
       case 6:
         visitor.clear()
         print("visitor data clear successfully")
       case 7:
         print("Exit Successfully......")
       case __:
         print("You entered wrong choice")


