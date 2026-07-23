n=int(input("Enter the number="))
i=1
while i<=n:
    print("")
    j=1
    while j<=i-1:
        print(" ",end="")
        j=j+1
    k=1
    while k<=n*2-i*2+1:
        if i==1 or k==1 or k==n*2-i*2+1:
           print(k,end="")
        else:
            print(" ",end="")
        k=k+1

    i=i+1