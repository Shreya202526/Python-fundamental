n=int(input("Enter the n:"))
i=0
while i<n:
    print("")
    j=1
    while j<=i:
        if j==1 or i==j:
          print(j,end=" ")
        else:
          print(" ",end="")
        j=j+1
    i=i+1
i=n-2
while i>0:
    print("")
    j=1
    while j<=i:
        if j==1 or i==j:
            print(j,end=" ")
        else:
            print(" ",end="")
        j=j+1
    i=i-1