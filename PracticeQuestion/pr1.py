r1=int(input("Enter the number of rows: "))
c1=int(input("Enter the number of columns: "))
print("Enter the element of first matrix: ")
A=[]
for i in range(r1):
    row=[]
    for j in range(c1):
        row.append(int(input()))
    A.append(row)

r2=int(input("Enter the number of rows: "))
c2=int(input("Enter the number of columns: "))
print("Enter the element of first matrix: ")
B=[]
for i in range(r2):
    row=[]
    for j in range(c2):
        row.append(int(input()))
    B.append(row)
print(A)
print(B)

if c1!=r2:
    print("Multiplication not possible")
else:
    result=[]
    for i in range(r1):
        row=[]
        for j in range(c2):
            row.append(0)
        result.append(row)
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j]=result[i][j]+A[i][k]*B[k][j]
    print(result)