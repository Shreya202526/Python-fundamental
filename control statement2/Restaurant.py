'''12. Restaurant Bill with GST System

A restaurant applies GST based on the total bill amount:

* Up to ₹1000 → 5% GST
* ₹1001 to ₹5000 → 12% GST
* Above ₹5000 → 18% GST
  Additionally, if the bill exceeds ₹3000, a service charge of ₹200 is added.

Write a Python program to calculate the final bill.

Input:
Enter bill amount: 4000

Output:
Final Bill Amount: ₹4680'''


total_amount=int(input("enter bill amount:"))
if total_amount<=1000:
   gst=total_amount*(5/100)
   final=gst+total_amount
elif total_amount>=1001 and total_amount<=5000:
     if total_amount>=3000:
       gst=total_amount*(12/100)
       total_amount=total_amount+200
       final=gst+total_amount
     else: 
        gst=total_amount*(12/100)
        final=gst+total_amount
elif total_amount>=5000:
       gst=total_amount*(18/100)
       total_amount=total_amount+200
       final=gst+total_amount
print("Final Bill amoumt",final)



