'''14. Online Course Fee System

An online platform offers courses with fixed fees:

* Programming → ₹5000
* Design → ₹4000
* Marketing → ₹3000
  Discount is applied based on user type:
* Student → 20% discount
* Working Professional → 10% discount
* Others → No discount

Write a Python program to calculate final course fee.

Input:
Enter course category: Programming
Enter user type: Student

Output:
Final Course Fee: ₹4000'''


course=input("Enter course category:")
user=input("Enter user type:")
if course.lower()=="programming":
   if user.lower()=="student":
       discount=5000*(20/100)
       final=5000-discount
   elif user.lower()=="working professional":
       discount=5000*(10/100)
       final=5000-discount
   elif user.lower()=="others":
       final=5000
elif course.lower()=="design":
   if user.lower()=="student":
       discount=4000*(20/100)
       final=4000-discount
   elif user.lower()=="working professional":
       discount=4000*(10/100)
       final=4000-discount
   elif user.lower()=="others":
       final=4000
elif course.lower()=="marketing":
   if user.lower()=="student":
       discount=3000*(20/100)
       final=3000-discount
   elif user.lower()=="working professional":
       discount=3000*(10/100)
       final=3000-discount
   elif user.lower()=="others":
       final=3000
print("Final Course fee:",final)

