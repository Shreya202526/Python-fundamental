from model.account import Account


accounts=[]
n=int(input("Enter the no of account:"))
for i in n:
  account_no=int(input("Enter Account NUmber:"))
  customer_name=input("Enter Customer name:")
  balance=int(input("Enter Balance"))
  account=Account(account_no,customer_name,balance)
  accounts.append(account)

  
