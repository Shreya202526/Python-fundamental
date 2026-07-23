n=int(input("Enter the number="))
i=1
while i<=n:
    print("")
    k=1
    while k<=i-1:
        print(" ",end="")
        k=k+1
    j=1
    ch=65
    while j<=n-i+1:
          print(chr(ch),end="")
          j=j+1
          ch=ch+1
    i=i+1
