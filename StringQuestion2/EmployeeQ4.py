'''4.
Employee ID Validator

A company wants to validate employee IDs before storing them in the database.

Conditions:
- ID must start with "EMP"
- Total length should be 8
- Remaining characters should be digits only

Input:
Enter Employee ID: EMP10234

Output:
Valid Employee ID'''


employee=input("Enter Employee Id")
valid=1
if employee[0]=='E' and employee[1]=='M' and employee[2]=='P':
      i=3
      while i<len(employee):
           ch=employee[i]
           if not ch.isdigit():
              valid=0
          
           else:
                valid=1
           i=i+1
else:
    valid=0
if valid==1 and len(employee)==8:
   print("valid ID")
else:
   print("Invalid")

 
   
