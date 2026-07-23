password=input("Enter the password")
print(password)
upper=0
lower=0
digit=0
space=0
special=0
i=0
while i<len(password):
      ch=password[i]
      if ch>='A' and ch<='Z':
         upper=1
      elif ch>='a' and ch<='z':
         lower=1
      elif ch>='0' and ch<='9':
         digit=1
      elif ch==' ':
         space=1
      else:
         special=1
      i=i+1
if len(password)>=8 and len(password)<=15 and upper==1 and lower==1 and digit==1 and space==0 and special==1:
   print("Valid password")
else:
   print("Invalid")


