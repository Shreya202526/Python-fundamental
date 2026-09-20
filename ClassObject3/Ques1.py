# QNO 1: Bank Account Management System

# ABC Bank wants to develop a software application to manage customer accounts.

# Each customer has:

# Account Number
# Customer Name
# Account Balance

# A customer should be able to:

# Deposit money
# Withdraw money
# Check account balance
# Transfer money to another customer

# The bank also wants to maintain information that is common for all customers:

# Bank Name
# Interest Rate

# The bank management may change the interest rate in the future, and the change should apply to all customers.

# Additionally, the application should provide some utility operations:

# Validate whether an account number is valid.
# Calculate interest on a given amount.
# Generate a transaction ID.
# Requirements

# Class Variables

# bank_name
# interest_rate

# Instance Variables

# account_no
# customer_name
# balance

# Instance Methods

# deposit(amount)
# withdraw(amount)
# transfer_money(receiver, amount)
# display_balance()

# Class Methods

# change_interest_rate(new_rate)
# change_bank_name(new_name)
# display_bank_info()

# Static Methods

# validate_account_number(account_no)
# calculate_interest(amount, rate)
# generate_transaction_id()

# Sample Input
# Customer 1
# Account No : 1001
# Name       : deepika
# Balance    : 50000

# Customer 2
# Account No : 1002
# Name       : Priya
# Balance    : 30000

# Deposit Amount : 10000
# Transfer Amount : 15000
# New Interest Rate : 7.5
# Sample Output
# Customer : deepika
# Balance  : 45000

# Customer : Priya
# Balance  : 45000

# Bank Name      : ABC Bank
# Interest Rate  : 7.5%
# Transaction ID : TXN1025

# Task: Design a Python class named BankAccount and implement all the above methods using instance methods, class methods, and static methods appropriately.






class Bank:
    bank_name="ABC Bank"
    interest_rate=7.5
    def add_Customer(self,account_no,customer_name,balance):
        self.account=account_no
        self.customer_name=customer_name
        self.balance=balance
    def deposit(self,d_amount):
         self.amount=d_amount
    def withdraw(self,w_amount):
        self.withdraw=w_amount
    def transfer_money(self,receiver, t_amount):
         self.receiver=receiver
         self.t_amount=t_amount
    def display_balance(self):
        print("self.+")

b1=Bank()
b1.display_balance()




    

# change_interest_rate(new_rate)
# change_bank_name(new_name)
# display_bank_info()

# Static Methods

# validate_account_number(account_no)
# calculate_interest(amount, rate)
# generate_transaction_id()
