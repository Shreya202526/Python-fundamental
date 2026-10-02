
'''ASSIGNMENT 2 — BANK ACCOUNT MANAGEMENT SYSTEM
=============================================

A bank provides different types of accounts.

Create the following hierarchy:

Account
|
+-------- SavingsAccount
|
+-------- PremiumSavingsAccount

REQUIREMENTS:

1. Create a parent class Account.

Attributes:

* account_number
* customer_name
* balance

2. SavingsAccount should inherit from Account.

Additional attribute:

* interest_rate

3. PremiumSavingsAccount should inherit from SavingsAccount.

Additional attribute:

* cashback_percentage

4. Parent-class data must be initialized using super().

5. Create the following methods:

display_account()
deposit()
withdraw()

6. Override display_account() in SavingsAccount.

7. Override display_account() again in PremiumSavingsAccount.

8. Each overridden method must call the parent method using super().

9. Demonstrate multilevel inheritance.

10. Balance must be encapsulated using:

@property
@balance.setter
@balance.deleter

11. Balance cannot be negative.

12. Read all data from the user.

INPUT:

Enter Account Number:
Enter Customer Name:
Enter Initial Balance:
Enter Account Type:

1. Savings Account
2. Premium Savings Account

For Savings Account:

Enter Interest Rate:

For Premium Savings Account:

Enter Interest Rate:
Enter Cashback Percentage:

Then ask:

Enter amount to deposit:
Enter amount to withdraw:

SAMPLE INPUT:

Enter Account Number: 1001
Enter Customer Name: Amit
Enter Initial Balance: 25000
Enter Account Type: 2
Enter Interest Rate: 7
Enter Cashback Percentage: 2
Enter amount to deposit: 5000
Enter amount to withdraw: 3000

EXPECTED OUTPUT:

## Account Details

Account Number: 1001
Customer Name: Amit
Balance: 25000

Account Type: Premium Savings Account
Interest Rate: 7%
Cashback Percentage: 2%

After Deposit:
Balance: 30000

After Withdrawal:
Balance: 27000'''

class Account:
    def __init__(self,acc_no,customer_name,balance):
        self.acc_no=acc_no
        self.customer_name=customer_name
        self.balance=balance
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self,new):
        if new<0:
            raise ValueError("Salary must be greater than 0")
        self.__balance=new
    @balance.deleter
    def balance(self):
        print("Deleting the balance")
        del self.__balance

    def display_account(self):
        print("Account  no. :",self.acc_no)
        print("Customer name:",self.customer_name)
        print("Balance:",self.balance)

    def deposit(self,amount):
        self.balance=self.balance+amount
        print("After Deposit:")
        print("Balance:",self.balance)
    def withdraw(self,amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than 0")

        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance=self.balance-amount
        print("After Withdrawing:")
        print("Balance:",self.balance)



class SavingsAccount(Account):
    def __init__(self,acc_no,customer,balance,interest_rate):
        super().__init__(acc_no,customer,balance)
        self.interest_rate=interest_rate
    def display_account(self):
        super().display_account()
        print("Account Type: Savings Account")
        print("Interest Rate:", self.interest_rate, "%")



class PremiumSavingsAccount(SavingsAccount):
    def __init__(self,acc_no,customer,balance,interest_rate,cashback_percentage):
        super().__init__(acc_no,customer,balance,interest_rate)
        self.cashback_percentage=cashback_percentage
    def display_account(self):
        super().display_account()
        print("Account Type: Premium Savings Account")
        print("Cashback Percentage:", self.cashback_percentage, "%")



no=int(input("Enter Account Number:"))
name=input("Enter Customer Name:")
inibalance=float(input("Enter Initial Balance:"))
type=input("Enter Account Type:(Savings Account/Premium Savings Account)")
if type=="Savings Account":
    interestrate=int(input("Enter Interest Rate:"))
    account = SavingsAccount(no, name, inibalance, interestrate)
elif type=="Premium Savings Account":
    interestrate=int(input("Enter Interest Rate:"))
    cashbackpercentage=int(input("Enter Cashback percentage:"))
    account = PremiumSavingsAccount(no, name, inibalance, interestrate, cashbackpercentage)

account.display_account()
deposit = float(input("Enter amount to deposit: "))
account.deposit(deposit)
withdraw = float(input("Enter amount to withdraw: "))
account.withdraw(withdraw)