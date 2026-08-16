'''4.
Palindrome Number List Checker
Scenario

A system checks lucky numbers which are palindromes.

Requirements
Check palindrome numbers
Store palindrome numbers in list
Count palindrome numbers
Find largest palindrome
Sort palindrome list
Test Cases

Input:
[121, 131, 20, 44, 55, 100]

Output:

Palindromes: [121, 131, 44, 55]
Count: 4
Largest: 131
Sorted: [44, 55, 121, 131]'''
n=int(input("Enter the string="))
nums=[]
pallindrome=[]
for i in range(n):
    x=int(input("Enter Element="))
    nums.append(x)
for x in nums:
    x2=x
    r=0
    for i in range(len(str(x)),0,-1):
     d=x%10
     r=r*10+d
     x=x//10
    if x2==r:
      pallindrome.append(x2)
print("Pallindroem:",pallindrome)
print("Count:",len(pallindrome))
largest=pallindrome[0]
for x in pallindrome:
   if x>largest:
      largest=x
print("Largest:",largest)
pallindrome.sort()
print("Sorted list:",pallindrome)
