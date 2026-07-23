'''1. Remove All Special Characters from a String

Online Banking Customer Data Cleaning System

A private bank has launched a new online account opening portal. While entering customer details, many users accidentally type unnecessary symbols, emojis, hashtags, dollar signs, and special characters in their names and addresses.

Before storing the data into the database, the bank wants a Python program that removes all unwanted special characters and keeps only:

* Alphabets
* Numbers
* Spaces

The cleaned value should be stored back into the original string variable.

Input:

Deepika@@ Padukone!! 123
Output:
Deepika Padukone 123
Input:
Ajay###Singh$$$
Output: 
AjaySingh
'''


s=input("Enter the string")
result="" 
i=0
while i<len(s):
      if s[i]>='a' and s[i]<='z':
         result=result+s[i]
      elif s[i]>='A' and s[i]<='Z' :
          result=result+s[i]
      elif s[i]>='0' and s[i]<='9':
         result=result+s[i]
      elif s[i]==" ":
          result=result+s[i]
      else:
          result=result
      i=i+1
print(result)

