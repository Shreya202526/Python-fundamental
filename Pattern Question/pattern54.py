n=int(input("Enter the number="))
i=1
while i<=n:
    print("")
    k=1
    while k<=i-1:
        print(" ",end="")
        k=k+1
    j=1
    ch=65
    while j<=n-i+1:
        if i==1 or j==1 or i+j==n+1:
            print(chr(ch),end="")
        else:
            print("_",end="")
        j=j+1
        ch=ch+1
    i=i+1
