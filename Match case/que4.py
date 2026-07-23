
'''4. Electricity Bill Management System

You are developing an Electricity Bill Management System for a power distribution company. The system helps calculate electricity bills for customers based on their unit consumption.

Sometimes, the operator may try to calculate the bill or apply surcharge before entering the number of units consumed. Your system must handle such situations properly.

👉 Important Condition:
If units are not entered, the system should display:
"Please enter units consumed first"
and should not perform further calculations.

The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

Menu Options:
1 → Enter Units Consumed
2 → Calculate Bill Amount

* First 100 units → ₹5 per unit
* Next 100 units → ₹7 per unit
* Above 200 units → ₹10 * per unit
  3 → Apply Surcharge
* If bill > 2000 → 10% surcharge
* Otherwise → 5% surcharge
  4 → Display Final Bill
  5 → Exit'''

unit=0
final=0
bill=0
sucharge=0
while True:
    print("Menu Options")
    print("1 → Enter Units Consumed")
    print("2 → Calculate Bill Amount")
    print("3 → Apply Surcharge")
    print("4 → Display Final Bill")
    print("5 → Exit")
    menu=int(input("Enter the Options="))
    match menu:
          case 1:
              unit=int(input("Enter the units "))
              print("units entered sucessfully......")
          case 2:
              if unit==0:
                print("please enter unit first===")
              else:  
                  if unit<=100:
                     bill=unit*5
                  elif unit>=100 and unit<=200:
                     bill=(unit-100)*7+100
                  elif unit>=200:
                     bill=(unit-200)*10+500+700
                  print(bill)
          case 3:
               if bill==0:
                  print("Firstly need to find bill")
               else:
                   if bill>2000:
                       surcharge=bill*(10/100)
                       print("Surcharge",int(surcharge))
                   else:
                       surcharge=bill*(5/100) 
                       print("Surcharge",int(surcharge))
          case 4: 
            if surcharge==0:
                      print("You Need to find further value") 
            else:
                final=bill+surcharge
                print("---Final Bill----")
                print("Units",unit)
                print("Bill amount",bill)
                print("surcharge",surcharge)
                print("Final Bill=",final)
          case __:
              print("Invalid case")
              break
    again=input("do you want to continue.....yes/no")
    match again: 
           case "yes":
                 continue
           case "no":
                 break
           case __ :
                print("kuch bhiiiii") 
                break 
print("Done")       
  


          


              





