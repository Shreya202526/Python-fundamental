'''Assignment 1: Restaurant Bill Split

A group of friends went to a restaurant. The restaurant adds GST and service charge to the bill, and then the total is divided equally.

Input:
Total bill amount = 2500
GST = 5%
Service charge = 10%
Number of friends = 4

Expected Output:
Final Bill = 2875.0
Each Person Pays = 718.75

---'''



total_bill=int(input("Total bill amount="))
gst=int(input("GST="))
sc=int(input("service charge="))
friends=int(input("Number of friends="))
gst =total_bill*(gst/100)
sc=total_bill*(sc/100)
final_bill=total_bill+gst+sc
person_pay=final_bill/friends
print(f"Final Bill={final_bill}\n Each person Pays={person_pay}")

