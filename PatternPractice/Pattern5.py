n=int(input("Enter the n="))
i=1
while i<=n:
    print("")
    j=1
    while j<=i:
        print("*",end="")
        j=j+1
    i=i+1
i=n-1
while i>=1:
    print("") 
    j=1
    while j<=i:
        print("*",end="")
        j=j+1
    i=i-1