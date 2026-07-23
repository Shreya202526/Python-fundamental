'''1.
Email Username Validator

A company wants to check whether an employee email username is valid before creating an official account.

Conditions:
- Username should start with a letter
- Username can contain letters, digits, underscore (_)
- No spaces allowed
- Length should be between 5 and 12 characters

Input:
Enter username: ajay_123

Output:
Valid Usernsame'''


username=input("Enter username=")
print(username)
letter=0
digit=0
space=0
special=0
i=0
while i<len(username):
      ch=username[i]
      if ch.isalpha():
         letter=1
      elif ch.isdigit():
         digit=1
      elif ch==" ":
         space=1
      else:
         special=1
      i=i+1
if len(username)>=5 and len(username)<=12 and letter==1 and digit==1 and space!=1 and special==1:
   print("valid Username")
else:
   print("invalid Username")
   
       

      







