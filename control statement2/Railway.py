'''11. Railway Ticket Fare System


A railway system calculates ticket fare based on distance and travel class:

* Distance ≤100 km:
  Sleeper → ₹100, AC → ₹200
* Distance 101–500 km:
  Sleeper → ₹300, AC → ₹600
* Distance >500 km:
  Sleeper → ₹500, AC → ₹1000

Write a Python program to calculate ticket fare.

Input:
Enter distance: 350
Enter class: AC

Output:
Total Fare: ₹600'''



distance=int(input("Enter Distance:"))
travel_class=input("Enter class:")
if distance<=100:
   if travel_class.upper()=="AC":
      print("Total fare:rs200")
   else:
      print("Total fare:rs100")
elif distance>=101 and distance<=500:
   if travel_class.upper()=="AC":
      print("Total fare:rs600")
   else:
      print("Total fare:rs300")
elif distance>=500:
   if travel_class.upper()=="AC":
      print("Total fare:rs1000")
   else:
      print("Total fare:rs500")

