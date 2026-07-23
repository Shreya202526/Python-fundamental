'''*12. Multiplication of Digits*
A puzzle game calculates a score by multiplying all digits of a number together. After calculating the score, the game also checks whether the final score is even or odd to assign a bonus.
Write a program to *find the product of all digits of a number using loops and then check whether the result is even or odd*.

Input: 1234
Output: 24
Even'''
    



'''num=int(input("Enter="))
mult=1
for i in range(len(str(num))):
    n=num%10
    mult=mult*n
    num=num//10
print("output=",mult)
if(mult%2==0):
     print("Even")
else:
     print("Odd")'''




num=int(input("Enter="))
mult=1
while num>0:
    n=num%10
    mult=mult*n
    num=num//10
print("output=",mult)
if(mult%2==0):
     print("Even")
else:
     print("Odd")
