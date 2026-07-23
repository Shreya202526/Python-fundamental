n=int(input("Enter the number="))
i=1
while i<=n:
    print("")
    k=1
    while k<=n-i:
        print(" ",end="")
        k=k+1
    j=1
    while j<=i-1+i:
        if i==1 or j==1  or i==n or j==i-1+i:
           print("1",end="")
        else:
            print("*",end="")
        j=j+1
    i=i+1
