'''3. Perfect Number Reward System
A gaming company rewards users if entered number is a Perfect Number.
(Perfect Number = sum of proper factors equals number)
Write a program using for-else loop to:
- Find sum of proper factors
- If sum equals number print Reward Unlocked
- Else print Try Again
Input:
6
Output:
Reward Unlocked'''
n=int(input("Enter the number="))
factor=0
for i in range(1,n):
      if n%i==0:
         factor=factor+i
else:
    print("Sum of factor",factor)
    if factor==n:
       print("reward unlocked")  
    else:
       print("locked")     

     
     

