n=int(input("Enter the number="))
i=1
while i<=n:
    print("")
    j=1
    while j<=i-1:
        print(" ",end="")
        j=j+1
    k=1
    ch=65
    while k<=n-i+1:
        print(chr(ch),end=" ")
        k=k+1
        ch=ch+1
    i=i+1