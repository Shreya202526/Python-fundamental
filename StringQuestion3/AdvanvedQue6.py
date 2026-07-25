'''6.
 Advanced Student Registration Data Processing System

A national university is developing an intelligent registration portal.Students enter registration codes using uppercase letters, lowercaseletters, digits, and special symbols. Due toinconsistent data entry,the administration wants the system to standardize and process theinformation before storing it.Conditions: - Ignore all special characters (@ # $ % & * - _) - Separate alphabets and digits - Convert all alphabets to lowercase - Removeduplicate alphabets - Arrange alphabets in ascending order - Arrange digits in descending order - Display alphabets first and digits later -
If no digits are found, display “No Digits Found”'''

code=input("Enter registration code:")
letters=""
digits=""
i=0
result=""
while i<len(code):
   ch=code[i]
   if ch>='a' and ch<='z' or ch>='A' and ch<='Z':
      if ch not in letters:
         letters+=ch.lower()
   elif ch>='0' and ch<='9':
         digits+=ch
   i+=1
if digits=="":
   print("No Digits Found")
else:
 for i in (sorted(letters)):
    result=result+i 
 for j in (sorted(digits)):
     result=result+j      

print("Result:",result)