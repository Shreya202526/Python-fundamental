'''6.
Railway Ticket PNR Analyzer

A railway department wants to verify whether a PNR number is valid.

Conditions:
- PNR must start with "PNR"
- Total length should be 12 characters
- Remaining characters should be digits

Input:
Enter PNR: PNR123456789

Output:
Valid PNR Number'''
s=input("Enter PNR=")
count=0
if len(s)==12:
   if s[0]=='P' and s[1]=='N' and s[2]=='R':
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

               

