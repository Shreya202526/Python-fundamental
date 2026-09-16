'''Assignment 3: Bank Account Operations
 A bank wants to perform basic operations on a customer's account.

Create a class BankAccount with the following attributes:

Account number

Account holder name

Balance

Create the following methods:

deposit() – Add an amount to the balance.

withdraw() – Subtract an amount from the balance.

display_account() – Display account details and final balance.

Sample data:

Account Number: 1001
Account Holder: Rahul
Opening Balance: 25000
Deposit: 5000
Withdrawal: 3000

Expected result:

Final Balance: 27000'''

class BankAccount:
    def set(self,acc_no,holder_name,balance):
        self.acc_no=acc_no
        self.name=holder_name
        self.balance=balance

    def deposit(self,amt):
        self.amt=amt
        self.balance=self.balance+self.amt

    def withdraw(self,wd):
        self.wd=wd
        self.balance=self.balance-self.wd

    def display_salary(self):
        print("Account Number:",self.acc_no)
        print("Account Holder:",self.name)
        print("Opening Balance",self.balance)
        print("Deposit:",self.amt)
        print("Withdrawal:",self.wd)
        print("Final balance",self.balance)

a1=BankAccount()
a1.set(1001,"Shreya",25000,)
a1.deposit(5000)
a1.withdraw(3000)
a1.display_salary()