'''Write a program to find out the sum of all integer between 100 and 200 which are divisible by 9'''


a=int(input("Enter first number="))
b=int(input("Enter Second number="))
i=a
sum=0
for i in range(a,b+1):
    if i%9==0:
        sum=sum+i
        print(i)
print(sum)
    