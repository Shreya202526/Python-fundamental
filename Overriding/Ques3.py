'''Assignment 3 – Bank Account System

Create a parent class BankAccount with:

account_no
holder_name
balance

Create two child classes:

SavingsAccount
CurrentAccount
Requirements
Take account details from the user.
Use super() to initialize the common attributes.
Create a method calculate_interest() in the parent class.
Override this method in both child classes.
Savings Account gets 5% interest.
Current Account gets 2% interest.
Display the account details and calculated interest.
Sample Input
Enter Account Number: 1001
Enter Holder Name: Amit
Enter Balance: 50000
Enter Account Type: Savings


Expected Output
----- Account Details -----
Account Number : 1001
Holder Name    : Amit
Balance        : 50000
Account Type   : Savings
Interest Rate  : 5%
Interest       : 2500
Amount After Interest : 52500'''

class BankAccount:
    def __init__(self,account_no,holder_name,balance):
        self.account_no=account_no
        self.holder_name=holder_name
        self.balance=balance

    def calculate_interest(self,interest_rate):
        return 0
class SavingsAccount(BankAccount):
     def __init__(self,account_no,holder_name,balance):
         super().__init__(account_no,holder_name,balance)
     def calculate_interest(self):
             return self.balance*0.05

     
class CurrentAccount(BankAccount):
    def __init__(self,account_no,holder_name,balance):
         super().__init__(account_no,holder_name,balance)
    def calculate_interest(self):
            return self.balance*0.02
account_no=int(input("Enter Account Number:"))
holder_name=input("Enter Holder Name:")
balance=int(input("Enter balance:"))
acc_type=input("Enter User Type:")
if acc_type=="Savings":
     acc=SavingsAccount(account_no,holder_name,balance)
     interest_rate=5

elif acc_type=="Current":
     acc=CurrentAccount(account_no,holder_name,balance)
     interest_rate=2

else:
     print("You entered wrong account")

interest=acc.calculate_interest()
print("--------Account Details----------")
print("Account Number : ",acc.account_no)
print("Holder Name    : ",acc.holder_name)
print("Balance        : ",acc.balance)
print("Account Type   : ",acc_type)
print("Interest Rate  : ",str(interest_rate),"%")
print("Interest       : ",interest)
print("Amount After Interest :", acc.balance+balance)
