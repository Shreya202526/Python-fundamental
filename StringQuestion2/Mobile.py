'''2.
Mobile Number Digit Counter

A telecom company wants to count how many digits are present in a customer contact number entered with spaces or symbols.

Input:
Enter contact number: +91 98765-43210

Output:
Total digits: 12'''


contact=input("Enter Contact number:")
print(contact)
count=0
i=0
while i<len(contact):
      ch=contact[i]
      if ch.isdigit():
         count=count+1
      i=i+1
print(count)
         
