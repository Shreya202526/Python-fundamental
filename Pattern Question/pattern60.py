n=int(input("Enter the number="))
i=1
while i<=n:
    print("")
    k=1
    while k<=n-i:
        print("s",end="")
        k=k+1
    j=1
    while j<=i:
          if j==1 or i==1 or  i==n or j==i:
            print("X" ,end=" ")
          else:
              print("_",end=" ")
          j=j+1
    i=i+1
