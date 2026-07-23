'''a=int(input("Enter the number"))
b=int(input("Enter the number"))
for i in range(a,b+1):
    n=i
    x=True
    if n>2:
       for j in range(2,n//2+1):
           if n%j==0:
              x=False
              break
       if x==True:
               print(n) '''

a=int(input("Enter the number"))
b=int(input("Enter the number"))
for i in range(a,b+1):
     n=i
     if n>2:
        for j in range(2,n//2+1):
            if n%j==0:
               break
        else:
            print(n) 
     
        