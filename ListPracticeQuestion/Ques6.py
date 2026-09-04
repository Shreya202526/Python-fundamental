'''Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"'''
'''
a=input("Enter the number1: ")
b=input("Enter the number2: ")
i=0
a2=0
b2=0
for i in range(len(a)-1,-1,-1):
    a2+=int(a[i])*2**i
    i+=1
print(a2)
i=0
for i in range(len(b)-1,-1,-1):
    b2+=int(b[i])*2**i
    i+=1
print(b2)
while b:
    carry=a&b
    a=a^b
    b=carry<<1
'''

a=input("Enter the number1: ")
b=input("Enter the number2: ")
res=bin(int(a,2)+int(b,2))
print(res[2:])
