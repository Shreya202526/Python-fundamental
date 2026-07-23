'''7.
Vehicle Number Plate Checker

The traffic department wants to validate vehicle registration numbers.

Conditions:
- First 2 characters should be alphabets
- Next 2 should be digits
- Total length should be 10

Input:
Enter vehicle number: MP04AB1234

Output:
Valid Vehicle Number'''



s=input("Enter PNR=")
count=0
if len(s)==10:
   if s[0]=='M' and s[1]=='P' :
     i=3
     while i<len(s):
           if s[i]>='0' and s[i]<='9':
               count=count+1 
           else: 
              print("Invalid PNR")
           i=i+1
if count==9:
    print("Valid PNR")
else:
    print("Invalid PNR")
