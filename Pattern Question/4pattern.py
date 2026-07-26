'''
*****
####
***
##
*


n=int(input("Enter the Number="))
i=1
while i<=n:
    print("")
    j=1
    while j<=n-i+1:
        if i%2==0:
            print("#",end="")
        else:
            print("*",end="")
        j=j+1
    i=i+1


55555
4  4
3 3
22
1


n=int(input("Enter the n="))
i=1
ch=n
while i<=n:
     print("")
     j=1
     while j<=n-i+1:
         if i==1 or j==1 or n+1==i+j:
             print(ch,end="")
         else:
            print(" ",end="")
         j=j+1
     ch=ch-1
     i=i+1
     '''
'''
         *
         **
         ****
         *******
         ***********
            
n=int(input("Enter number="))
i=1
str=1
while i<=n:
    print("")
    j=1
    while j<=str:
        print("*",end="")
        j=j+1
    str=str+i
    i=i+1
  
         '''

n=int(input("enter the number"))
i=1
str=1
while i<=n:
    # print("")
    # j=1
    # while j<=i-1:
    #     print(" ",end="")
    #     j=j+1
    k=1 
    while k<=str:
        print("*",end= "")  
        k=k+1
    print()
    str=str+i
    i=i+1