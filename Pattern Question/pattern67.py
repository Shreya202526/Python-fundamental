n=int(input("Enter the number="))
i=1
while i<=n:
    print("")
    k=1
    while k<=i-1:
        print("s",end="")
        k=k+1
    j=1
    while j<=2*n-2*i+1:
        print("*",end="")
        j=j+1
    i=i+1
