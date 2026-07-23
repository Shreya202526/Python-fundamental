'''2. An e-commerce website provides discounts based on the cart value and user type.
The system should take cart value and user type (premium or regular) as input.
 If the cart value is greater than or equal to 5000, then check the user type. If the user is premium,
 apply a 20% discount; otherwise, apply a 10% discount. If the cart value is less than 5000,
then check if it is greater than or equal to 2000. If yes, apply a 5% discount; otherwise,
no discount is applied. Display the final payable amount.

Input:
Cart Value = 6000
User Type = Premium'''



cart=int(input("Cart Value="))
usertype=input("User Type=")
if cart>=5000:
   if usertype.lower()=="premium":
      discount=cart*(20/100)
      final=cart-discount
   else:
      discount=cart*(10/1000)
      final=cart-discount
else:
        if cart>=2000:
           discount=cart*(5/100)
           final=cart+discount
        else:
           print("No discount applied")
print("Final amount",final)


            