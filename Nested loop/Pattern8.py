n=int(input("Enter number="))
i=1
while i<=n:
    
    s=1
    while s<i:
         print(" ",end="")
         s=s+1
    j=n
    while j>=i:
          print(j,end="")
          
          j=j-1
    print()      
    i=i+1
