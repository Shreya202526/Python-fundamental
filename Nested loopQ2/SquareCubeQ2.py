'''WAP to print square ,cube ,and square root of all number from 1 to N'''


a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
i=a
sq=0
cube=0
sq_root=1
for i in range(a,b+1):
    sq=i**2
    print("Square Root",sq)
    cube=i**3
    print("Cube Root",cube)
