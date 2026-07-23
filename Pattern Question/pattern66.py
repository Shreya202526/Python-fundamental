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
        if j==i:
            print("#",end="")
        else:
           print("*",end="")
        j=j+1
    i=i+1
