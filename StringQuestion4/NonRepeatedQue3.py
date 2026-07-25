'''3. Find the First Non-Repeated Character
Railway Ticket Fraud Detection System
The railway department generates ticket reference IDs automatically.

Sometimes, due to technical issues, many characters get repeated inside the ticket ID.

The department wants a Python program that finds the first character that appears only once in the string.

Example 1

Input:
aabbccddefg
Output:'''

s=input("Enter the String=")
i=0
while i<len(s):
      ch=s[i]
      j=0
      count=0
      while j<len(s):
            if ch==s[j]:
                  count=count+1
                  
            j=j+1
      i=i+1
if count==1:
   print(ch,end=" ")
   


