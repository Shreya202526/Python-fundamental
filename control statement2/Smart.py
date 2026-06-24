'''15. Smart Parking System

A smart parking system charges based on vehicle type and parking duration:

* Bike → ₹10/hour
* Car → ₹20/hour
* Bus → ₹50/hour
  If parking duration exceeds 5 hours, an additional ₹100 penalty is applied.

Write a Python program to calculate total parking fee.

Input:
Enter vehicle type: Car
Enter hours parked: 6

Output:
Total Parking Fee: ₹220'''


vehicle=input("Enter Vehicle type:")
hours=int(input("Enter hours parkes:"))
if vehicle.lower()=="bike":
    if hours>=5:
       fee=hours*10+100
    else:
       fee=hours*10
elif vehicle.lower()=="car":
       if hours>=5:
          fee=hours*20+100
       else:
          fee=hours*20
elif vehicle.lower()=="bus":
       if hours>=5:
          fee=hours*50+100
       else:
          fee=hours*50
print("Total parking fee:",fee) 

