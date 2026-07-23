
'''
ABCDE
A  D
A C
AB
A


n=int(input("Enter the n="))
i=1
ch=65
while i<=n:
    print("")
    j=1
  
    while j<=n:
        if i==1 or j==1 or j==n-i+1:
           print(chr(ch),end="")
        else:
            print(" ",end="")
        j=j+1
    ch=ch+1
    i=i+1

55555
4  4
3 3
22
1

n=int(input("enter the n="))
i=1
k=n
while i<=n:
    print()
    j=1
    while j<=n:
        if i==1 or j==1 or j==n-i+1:
           print(k,end="")
        else:
            print(" ",end="")
        j=j+1
    k=k-1

    i=i+1
    '''
'''
123456
54321
1234
321
12
1

n=int(input("enter the number"))
i=1
while i<=n:
    print("")
    j=1
    k=n-i+1
    while j<=n-i+1:
        if i%2==0:
            print(k,end="")
        else:
          print(j,end="")
        j=j+1
        k=k-1
    i=i+1

*
**
****
*******
***********
















A
BCD
EFGHI
JKLMNOP


n=int(input("Enter the n="))
i=1
ch=65
while i<=n:
    print("")
    j=1
    while j<=i*2-1:
        print(chr(ch),end="")
        j=j+1
        ch=ch+1
    i=i+1
    
    
54321
5432
543
54
5
  

n=int(input("Enter the n="))
i=1
while i<=n:
    print("")
    j=1
    k=n
    while j<=n-i+1:
        print(k,end="")
        j=j+1
        k=k-1
    i=i+1
    

    


1
12
123
1234
12345

n=int(input("Enter the n="))
i=1
while i<=n:
    print("")
    j=1
    while j<=n-i:
            print(" ",end="")
            j=j+1
    k=1      
    while k<=i:
          print(k,end="")
          k=k+1
    i=i+1
    

1
22
333
4444
55555


n=int(input("Enter the n="))
i=1
while i<=n:
    print("")
    j=1
    while j<=n-i:
            print(" ",end="")
            j=j+1
    k=1      
    while k<=i:
          print(i,end="")
          k=k+1
    i=i+1
    
5
44
333
2222
11111


n=int(input("Enter the n="))
i=1
x=n
while i<=n:
    print("")
    j=1
    while j<=n-i:
            print(" ",end="")
            j=j+1
    k=1     
    while k<=i:
          print(x,end="")
          k=k+1
    x=x-1
    i=i+1




A
AB
ABC
ABCD
ABCDE


n=int(input("Enter the n="))
i=1
while i<=n:
    print("")
    j=1
    while j<=n-i:
            print(" ",end="")
            j=j+1
    k=1
    ch=65     
    while k<=i:
          print(chr(ch),end="")
          k=k+1
          ch=ch+1
    i=i+1
    '''


'''
     1
    11
   1*1
  1**1
 11111

n=int(input("Enter the n="))
i=1
while i<=n:
    print("")
    j=1
    while j<=n-i:
        print(" ",end="")
        j=j+1
    k=1
    while k<=i:
        if i==1 or i==n or k==1:
            print("1", end="")
        else:
            if k==i:
               print("1",end="")
            else:
               print("*",end="")
        k+=1 
    i+=1
    

           A
          AB
         A_C
        A__D
       ABCDE
       
'''
n=int(input("Enter the number="))
i=1
while i<=n:
    print("")
    j=1
    while j<=n-i:
        print("",end=" ")
        j+=1
    k=1
    ch=65
    while k<=i:
        if i==1 or i==n or k==1 or k==i:
            print(chr(ch),end="")
        else:
            print("_",end="")
        k=k+1
        ch=ch+1
    i+=1      



    



















