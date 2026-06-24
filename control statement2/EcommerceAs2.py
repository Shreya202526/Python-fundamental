'''4. E-Commerce Discount Engine


An online shopping platform provides discounts to customers based on their total purchase amount:

* Above ₹5000 → 20% discount
* ₹2000 to ₹5000 → 10% discount
* Below ₹2000 → 5% discount

Write a Python program to calculate the final amount after discount.

Input:
Enter purchase amount: 4500

Output:
Final Amount: ₹4050'''
   

amount=int(input("Enter Purchase amount:"))
if amount>=5000:
   discount=amount*(20/100)
   final=amount-discount
elif amount<=5000 and amount>=2000:
   discount=amount*(10/100)
   final=amount-discount
elif amount<=2000:
   discount=amount*(10/100)
   final=amount-discount
print("Final amount:",final) 
