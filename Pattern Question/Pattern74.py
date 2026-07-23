'''
x
xx
xxx
xxxx
xxx
xx
x
'''
n=int(input("Enter the n:"))
i=0
while i<n:
    print("")
    j=0
    while j<=i:
        print("x",end="")
        j=j+1
i=n-1
while i<n:
    print("")
    j=0
    while j<=i:
        print("x",end="")
        j=j+1
