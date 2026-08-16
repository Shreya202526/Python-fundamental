'''2.
Secure Password Analysis

A cybersecurity team wants to identify pairs of passwords having no common characters.

Problem Statement:

Given N strings, count the number of pairs that do not share any common character.

Example:

Input

N = 4
passwords[] = {"abc", "de", "fg", "ad"}

Output

3

Explanation

("abc","de")
("abc","fg")
("de","fg")'''

n=int(input("Enter the size of list="))
password=[]
for i in range(n):
    x=input("Enter Element=")
    password.append(x)
print(password)
c=0
for a in range(n):
    for b in range(a+1,n):
        same=False
        for x in range(a):
            if x in range(b):
                same=True
        if same==False:
            c+=1
print(c)


