'''Smart Banking System

Scenario:
You are developing a Smart Banking System for a bank to help customers perform basic banking operations such as deposit, withdrawal, balance checking, and interest calculation.

Sometimes, users may try to withdraw money or check balance before depositing any amount. Your system must handle such situations properly.

👉 Important Condition:
If no amount has been deposited yet, the system should display:
"No balance available. Please deposit first"
and should not allow withdrawal, balance check, or interest calculation.

The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

Menu Options:
1 → Deposit Money
2 → Withdraw Money
3 → Check Balance
4 → Apply Interest
* Balance > 50000 → 5% interest
* Otherwise → 3% interest
  5 → Exit'''
withdraw=0
deposit=0
while True:
    print("Menu Option")
    print("1 → Deposit Money")
    print("2 → Withdraw Money")
    print("3 → Check Balance")
    print("4 → Apply Interest")
    print("5 → Exit")
    menu=int(input("Enter the Menu Option="))
    match menu:
        case 1:
            deposit=int(input("Enter basic Salary"))
            print(" Amount Deposited successfully")
            current=deposit
        case 2:
            
            if deposit==0:
                print("No Balance Available please deposit") 
            else:  
                withdraw=int(input("Withdraw Amount")) 
                if  withdraw>=deposit:
                    print("No Sufficient Balance")
                else:
                    current=deposit-withdraw
                    print("Withdraw Successfully")
        case 3:
              if deposit==0 :
                 print("Zeroo balance")
              else:
                 print("Current balance",current)  
        case 4: 
               if current>=50000:
                  interest=current*5/100
               else:
                   interest=current*3/100
                   current=deposit+interest
                   print(" interst added=",int(interest)) 
                   print(" interst added=",int(current))            
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
print("Existing Thankyou")       
  

    

