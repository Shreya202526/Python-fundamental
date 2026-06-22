'''Your shopping cart total doesn’t include tax. A 12% GST is applied.

Write a Python program that:
- Accepts the cart total amount.
- Calculates 12% tax.
- Displays the tax and final total amount.

Example:
Cart = ₹2000
Tax = ₹240
Total = ₹2240'''



cart=int(input("Cart"))
tax=cart*12//100
total=cart+tax
print(f" Cart= rs{cart}\n Tax=rs{tax}\n Total=rs{total}")