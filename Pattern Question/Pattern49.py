n=int(input("Enter the number="))
i=1
while i<=n:
    print("")
    k=1
    while k<=n-i+1:
        print(" ",end="")
        k=k+1
    j=1
    while j<=i-1:
        if j%2==0:
            print("0",end="")
        else:
            print("1",end="")
        j=j+1
    i=i+1