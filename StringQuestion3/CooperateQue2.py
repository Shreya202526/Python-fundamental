'''.  Corporate Employee Short ID Generator

A multinational company wants to automatically generate short IDs for
employees while creating official email accounts. The system should take
the employee’s full name and create an ID using the first character of
each word.

Conditions: - Take first character of every word - Convert all
characters to uppercase

Input: Enter employee name: ajay singh thakur

Output: Employee Short ID: AST'''

s=input("Enter the String=")
new_string=""
for i in range(len(s)):
    if i==0 or s[i-1]==" ":
      new_string=new_string+s[i].upper()
print(new_string)











