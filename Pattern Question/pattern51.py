n=int(input("Enter the number="))
i=1
s=n
while i<=n:
    print("")
    k=1
    while k<=i-1:
        print(" ",end="")
        k=k+1
    j=1
    while j<=n-i+1:
         print(s,end="")
         j=j+1
    s=s-1
    i=i+1