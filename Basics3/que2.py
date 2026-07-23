'''Assignment 2: Mobile EMI Calculation

You purchased a mobile phone using EMI. After paying a down payment, the remaining amount includes interest and is divided into monthly installments.

Input:
Mobile price = 30000
Down payment = 5000
Interest rate = 10%
Months = 10

Expected Output:
Remaining Amount = 25000
Total with Interest = 27500
Monthly EMI = 2750.0'''


mob_price=int(input("Mobile price="))
down_payment=int(input("Down payment="))
Interest_rate=int(input("Interest rate="))
month=int(input("Months="))
rem_amt=mob_price-down_payment
interest=rem_amt*(Interest_rate/100)
total=rem_amt+interest
emi=total/month
print(f"Remaining Amount= {rem_amt}\n Total with interest={interest}\n Monthly EMI ={emi}")

