'''# 3. Secure Banking Transaction Analyzer

A banking server generates encrypted transaction IDs using letters and digits.

The fraud detection team wants a Python program to find the first digit that does not repeat in the transaction ID.

If no unique digit exists, print:

text
No unique digit found


### Input:

text
A122334455667789


### Output:

text
8'''

s=input("Enter the String")
result=""
for i in s:
    if '0'<=i<='9':
     count=0
     for j in s:
         if i==j:
            count+=1
     if count==1:
        result=i
        break
print(result)
