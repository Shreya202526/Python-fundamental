'''5. Website URL Verification System

A software company is developing an automated website registration
portal. Before saving a website address, the system must verify whether
the URL follows the required company format.

Conditions: - Must start with www - Must end with .com

Input: Enter website: www.amazon.com

Output: Valid Website'''



s=input("Enter website:")
valid=0
i=0
while i<len(s):
   if s[:3]=='www' or s[::-1]==".com":
      valid=1
   else:
      valid=0
   i=i+1
if valid==1:
   print("Valid Website")
else:
  print("Invalid Website")
      
      
