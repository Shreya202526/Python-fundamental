'''matrix=[
    [1,2,3],
    [32,4,8],
    [9,66,77]
    ]
for row in matrix:
    print(row)

matrix=[
    [1,2,3],
    [32,4,8],
    [9,66,77]
    ]
for row in matrix:
    for val in row:
        if val%2==0:
         print(val,end=" ")
    print()'''


row=int(input("Enter the size of row"))
cols=int(input("Enter the size of column"))
matrix=[]
print("Enter the elements of elements")
for i in range(row):
 rows=[]
 for j in range(cols):
   rows.append(int(input()))
 matrix.append(rows)
print("matrix elements are",matrix)
for row in matrix:
  for val in row:
    print(val,end=" ")
  print()