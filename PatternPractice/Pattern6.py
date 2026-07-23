n=int(input("Enter the num="))
i=1
while i<=n:
    print("")
    j=1
    while j<=n-i:
          print(" ",end="")
          j=j+1
    k=n
    while k>=n-i+1:
         print("*",end="")
         k=k-1
    i=i+1