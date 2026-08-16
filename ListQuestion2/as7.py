'''.
Factory Production – Factorial Expansion List

Problem Statement
A factory produces items where production capacity is defined using factorial growth.

Given a list of numbers, replace each number with its factorial value.

Then perform analysis on the resulting list.

Tasks:

Convert each element to factorial
Find sum of all factorial values
Find maximum factorial value
Count how many factorial values are even

Input:
A list of integers

Example 1

Input:
[3, 4, 5]

Processing:
3! = 6
4! = 24
5! = 120

Output:
[6, 24, 120]
Sum = 150
Max = 120
Even Count = 3'''


n=int(input("Enter the length of list="))
arr=[]
factorial=[]
for i in range(n):
    x=int(input("Enter the element="))
    arr.append(x)
print(arr)
for x in arr:
    print(x)
    fact=1
    for i in range(1,x+1):
        fact*=i
    factorial.append(fact)
print("Factorial List:",factorial)
max=-1
sums=0
for x in factorial:
    sums+=x
    if x>max:
        max=x
print("Sum=",sums)
print("maximum",max)
print("Count",len(factorial))
