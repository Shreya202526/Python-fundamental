n=int(input("Enter the number="))
i=1
while i<=n:
    print("")
    k=1
    while k<=i-1:
        print(" ",end="")
        k=k+1
    j=1
    while j<=n-i+1:
        if  i==1 or j==1 or  i+j==n+1:
            print(j,end="")
        else:
          print("_",end="")
        j=j+1
    i=i+1

