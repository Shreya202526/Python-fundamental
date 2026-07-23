'''2.
 Employee Salary Processor
Scenario:
You are developing an Employee Salary Processing System for a company’s HR department.
 The system is used to manage and calculate employee salary details such as allowances, 
 tax deductions, and final payable salary.
The HR staff may not always follow the correct sequence while using the system. For
 example, they might try to calculate net salary or tax before entering the basic salary. 
 Your program must handle such situations properly
👉 Important Condition:
If the Basic Salary is not entered, the system should display:
"Please enter basic salary first"
and should not perform any further calculations.

The system should be menu-driven and must continue running until the user selects Exit.
 All operations should be handled using match-case.

Menu Options:
1 → Enter Basic Salary
2 → Calculate HRA (20%) and DA (10%)
3 → Calculate Net Salary
4 → Tax Deduction

* Salary > 50000 → 10% tax
* Otherwise → 5% tax
  5 → Display Salary Slip
  6 → Exit'''

salary=0
HRA=0
DA=0
while True:
    print("Menu Option")
    print("1 → Enter Basic Salary")
    print("2 → Calculate HRA (20%) and DA (10%)")
    print("3 → Calculate Net Salary")
    print("4 → Tax Deduction")
    print("5 → Display Salary Slip")
    print("6 → Exit")
    menu=int(input("Enter the Menu Option="))
    match menu:
        case 1:
            salary=int(input("Enter basic Salary"))
            print("Basic Salary Recorded successfully")
        case 2:
            if salary==0:
                print("Please enter basic salary first") 
            else:   
                   HRA=int(salary*(20/100))
                   DA=int(salary*(10/100))
                   print("HRA=",HRA)
                   print("DA",DA)
        case 3:
                 HRA=int(salary*(20/100))
                 DA=int(salary*(10/100))
                 Net_salary=HRA+DA+salary
                 print("Net salary(before tax)=",int(Net_salary))   
        case 4: 
               HRA=int(salary*(20/100))
               DA=int(salary*(10/100))
               Net_salary=HRA+DA+salary 
               if Net_salary>=50000:
                  tax=Net_salary*10/100
               else:
                   tax=Net_salary*5/100
               print("Tax=",int(tax)) 
               final=Net_salary-tax
        case 5:
               HRA=int(salary*(20/100))
               DA=int(salary*(10/100))
               Net_salary=HRA+DA+salary 
               if Net_salary>=50000:
                  tax=Net_salary*10/100
               else:
                   tax=Net_salary*5/100
               final=Net_salary-tax
               print("---Salary slip----")
               print("HRA:",HRA)
               print("DA:",DA)
               print("Net salary:",Net_salary)
               print("Tax:",tax)
               print("final Salary:",int(final))
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
  

    
