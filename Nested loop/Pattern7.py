n=int(input("Enter number="))
i=1
while i<=n:
      print("")
      j=1  
      while j<=n:
            if j>n-i:
               print("*",end="")
            else:
               print(" ",end="")
            j=j+1
      i=i+1
  