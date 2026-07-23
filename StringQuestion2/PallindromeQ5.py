'''5.
Palindrome Product Code Checker

A factory wants to identify whether a product code reads the same forward and backward.

Input:
Enter product code: MADAM

Output:
Palindrome Code

Input:
Enter product code: PRODUCT

Output:
Not a Palindrome Code'''


str1=input("Enter Product code=")
str2=""
for i in range(len(str1)-1,-1,-1):
    print(str1[i])
    str2=str2+str1[i]
if str1==str2:
   print("String is palindrome")
else:
  print("String is not pallindrome")