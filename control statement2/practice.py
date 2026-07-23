num=int(input("enter the number"))
reverse=0
i=1
while num>0:
    reverse=reverse*10+num%10
    num=num//10
print(reverse)

