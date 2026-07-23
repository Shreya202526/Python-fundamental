'''*****
n=int(input("Enter the n"))
i=1
while i<=n:
    print("*",end="")
    i=i+1'''



'''*
   *
   *
   *
   *

n=int(input("Enter the n"))
i=1
while i<=n:
    print("")
    j=1
    while j<=1:
        print("*",end="")
        j=j+1
    i=i+1
'''

''' 3. *
*
*
*
*

n=int(input("Enter the n"))
i=1
while i<=n:
    print("")
    j=1
    while j<=i-1:
           print("",end="")
           j=j+1
    k=1
    while k<=1:
          print("*",end="")
          k=k+1
    i=i+1'''

'''4.
*****
*****
*****
*****
****

n=int(input("Enter the n"))
i=1
while i<=n:
    print("")
    j=1
    while j<=n:
           print("*",end="")
           j=j+1
    i=i+1'''


'''5.12345
12345
12345
12345
12345
n=int(input("Enter the n"))
i=1
while i<=n:
    print("")
    j=1
    while j<=n:
           print(j,end="")
           j=j+1
    i=i+1



n=int(input("Enter the n"))
i=1
while i<=n:
    print("")
    j=1
    while j<=n:
           print(i,end="")
           j=j+1
    i=i+1'''



'''1
00
111
0000
11111

n=int(input("Enter the n"))
i=1
while i<=n:
    print("")
    j=1
    while j<=i:
           if j%2==0:
              print("0",end="")
           else :
              print("1",end="")
           j=j+1
    i=i+1'''
'''
*
**
***
****
*****

n=int(input("Enter the n"))
i=1
while i<=n:
    print("")
    j=1
    while j<=i:
              print("*",end="")
              j=j+1
    i=i+1
'''


'''1
12
123
1234
12345

n=int(input("Enter the n"))
i=1
while i<=n:
    print("")
    j=1
    while j<=i:
              print(j,end="")
              j=j+1
    i=i+1'''



''''''

'''n=int(input("Enter n"))
i=65
while i<=n:
      print()
      j=65
      while j<=i:
      
            print(chr(j),end=" ")
            j=j+1
      i=i+1

n=int(input("Enter n"))
i=97
while i<=n:
      print()
      j=97
      while j<=i:
      
            print(chr(j),end=" ")
            j=j+1
      i=i+1'''



'''1
01
101
0101
10101


n=int(input("Enter n"))
i=1
while i<=n:
      print("")
      j=1
      while j<=i+1:
            if i%2==0 and j%2==0:
               print("0",end="")
            elif j%2!=0 and i%2!=0:
                print("1",end="")
            j=j+1
      i=i+1



1
23
456
78910
n=int(input("Enter n"))
i=1
k=1
while i<=n:
      print("")
      j=1
      while j<=i:
            print(k,end="")
            k=k+1
            j=j+1
      i=i+1'''



'''A
BB
CCC
DDDD
EEEEE

n=int(input("Enter n"))
i=1
while i<=n:
      print("")
      j=1
      ch=65
      while j<=i:
            print(chr(ch),end="")
            j=j+1
      i=i+1'''
'''
*
* *
*  *
*   *
* * * * *

n=int(input("Enter n"))
i=1
while i<=n:
      print("")
      j=1
      while j<=i:
            if j==1 or (j==i) or (i==n):
                print("*",end="") 
            else:
                print(" ",end="")   
        
            j=j+1
      i=i+1


1
12
1 3
1  4
12345

n=int(input("Enter n"))
i=1
while i<=n:
      print("")
      j=1
      while j<=i:
            if j==1 or (j==i) or (i==n):
                print(j,end="") 
            else:
                print(" ",end="")   
        
            j=j+1
      i=i+1
'''

'''
1
22
3 3
4  4
55555

n=int(input("Enter n"))
i=1
while i<=n:
      print("")
      j=1
      while j<=i:
            if j==1 or (j==i) or (i==n):
                print(i,end="") 
            else:
                print(" ",end="")   
        
            j=j+1
      i=i+1
'''

'''
A
AB
A C
A  D
ABCDE


n=int(input("Enter n"))
i=1
while i<=n:
      print("")
      j=1
      ch=65
      while j<=i:
              if j==i or (j==1) or (i==n):
                print(chr(ch),end="")
                ch+=1 
              else:  
                print("8",end="")   
            
              j=j+1
      i=i+1'''

n=int(input("Enter n"))
i=1
while i<=n:
      print("")
      j=1
      ch=65
      while j<=i:
            print(chr(ch),end="")
            j=j+1
            ch=ch+1
      i=i+1











