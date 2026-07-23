'''
1
12
1 3
1  4
12345

n=int(input("Enter the n"))
i=1
while i<=n:
    print("")
    j=1
    while j<=i:
        if j==1 or j==i  or i==n:
            print(i,end="")
        else:
            print(" ",end="")
        j=j+1
    i=i+1
'''
'''
a
bc
d f
g  j
klmno


n=int(input("Enter the n"))
i=1
ch=97
while i<=n:
    print("")
    j=1
    while j<=i:
        
        if j==1 or j==i  or i==n:
            print(chr(ch),end="")
            ch=ch+1
        else:
            print(" ",end="")
        j=j+1
        
    i=i+1

    '''
'''
*
**
*@*
*@@*
* * * * *


n=int(input("Enter the n"))
i=1
while i<=n:
    print("")
    j=1
    while j<=i:
        
        if j==1 or j==i  or i==n:
            print("*",end="")
        else:
            print("# ",end="")
        j=j+1
        
    i=i+1
'''
'''
5
54
543
5432
54321


n=int(input("Enter ="))
i=1
while i<=n:
    print("")
    j=n
    while j>=n-i+1:
        print(j,end="")
        j=j-1
    i=i+1
'''

'''
*
*#
*#*
*#*#
*#*#*


n=int(input("Enter the number"))
i=1
while i<=5:
    print("")
    k=1
    while k<=i:
        if k%2==0:
            print("#",end="")
        else:
            print("*",end="")
        k=k+1
    i=i+1
    '''
'''
1
10
1 1
1  0
10101

n=int(input("Enter the number"))
i=1
while i<=5:
    print("")
    k=1
    while k<=i:
        if k==i or k==1 or i==n :
             if k%2==0:
                 print("0",end="")
             else:
                 print("1",end="")
        
        else:
           print(" ",end="")
        k=k+1
    i=i+1
    '''
'''
1
123
12345
1234567
123456789

n=int(input("enter the n"))
i=1
while i<=n:
     print("")
     j=1
     while j<=2*i-1:
          print(j,end="")
          j=j+1
     i=i+1
'''
'''
1
222
33333
4444444
555555555

n=int(input('Enter the n='))
i=1
while i<=n:
    print("")
    j=1
    while j<=2*i-1:
        print(i,end="")
        j=j+1
    i=i+1
'''

'''

***** 
**** 
***
**
* 


n=int(input("Enter the number"))
i=1
while i<=n:
    print("")
    j=0
    while j<=n-i:
        print("*",end="")
        j=j+1
    i=i+1



12345
1234
123
12
1


n=int(input("Enter the number"))
i=1
while i<=n:
    print("")
    j=1
    while j<=n-i:
        print(j,end="")
        j=j+1
    i=i+1
'''

'''
55555
4444
333
22
1

n=int(input("enter the number="))
i=n
while i>=1:
    print()
    j=1
    while j<=i:
        print(i,end="")
        j=j+1
    i=i-1
    
ABCDE
ABCD
ABC
AB
A

n=int(input("enter the number="))
i=n
while i>=1:
    print()
    j=1
    ch=65
    while j<=i:
        print(chr(ch),end="")
        j=j+1
        ch=ch+1
    i=i-1
'''

'''
EEEEE
DDDD
CCC
BB
A




n=int(input("enter the number="))
i=1
ch=64
+n
while i<=n:
    print()
    j=1
   
    while j<=n-i+1:
        print(chr(ch),end="")
        j=j+1
    ch=ch+1    
    i=i+1
    




*****
*  *
* *
**
*
'''

n=int(input("Enter the n="))
i=1
while i<=n:
    print(" ")
    j=1
    while j<=n:
          if j==1 or j==n-i+1 or i==1:
             
             print("*",end="")
          else:
              print(" ",end="")
          j=j+1 
    i=i+1












