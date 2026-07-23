n=int(input("Enter the num="))
i=1
while i<=2*n:
    print("")
    j=1
    x=2*n-i
    while j<=i:
        if i>=n:
         print("*",end="")
        else:
           print("*",end="")
           x=x-1
        j=j+1
    i=i+1