n=int(input("enter the number="))
i=1
while i<=n:
    print("")
    j=1
    while j<=i-1:
        print(" ",end="")
        j=j+1
    k=1
    while k<=n-i+1:
        print("*",end=" ")
        k=k+1
    i=i+1


