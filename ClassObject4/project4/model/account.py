

class Account:
    def __init__(self,account_no,customer_name,balance):
         self.account_no=account_no
         self.customer_name=customer_name
         self.balance=balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def display(self):
        print(self.account_no, self.customer_name, self.balance)



