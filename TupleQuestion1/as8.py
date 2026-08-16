'''8.
MATRIX PATTERN DETECTION SYSTEM

A satellite monitoring center stores signal strengths in matrix form. Engineers want to identify special patterns in the matrix.

Menu
1. Count Even Numbers Above Main Diagonal
2. Count Odd Numbers Below Main Diagonal
3. Display Boundary Elements
4. Exit
Requirements
Choice 1 – Count Even Numbers Above Main Diagonal

Count all even numbers where:

column > row
Choice 2 – Count Odd Numbers Below Main Diagonal

Count all odd numbers where:

row > column
Choice 3 – Display Boundary Elements

Display all elements present on:

First Row
Last Row
First Column
Last Column

without repeating corner elements.

Sample Input
1 2 3
4 5 6
7 8 9
Output
Even Numbers Above Main Diagonal = 2
(2, 6)

Odd Numbers Below Main Diagonal = 1
(7)

Boundary Elements:
1 2 3 6 9 8 7 4  '''

print("Menu")
print("1. Count Even Numbers Above Main Diagonal")
print("2. Count Odd Numbers Below Main Diagonal")
print("3. Display Boundary Elements")
print("4. Exit")
choice=int(input("Enter your choice:"))
match choice:
    case 1:
        row=int(input("Enter number of rows="))
        cols=int(input("Enter number of columns="))
        print("Enter elements of matrix A")
        matrix1=[]
        for i in range(row):
         rows=[]
         for j in range(cols):
            rows.append(int(input()))
         matrix1.append(rows)
        print("Enter Matrix A")
        for rows in matrix1:
            for val in rows:
                 print(val,end=" ")
            print()
        t=[]
        c=0
        for i in range(row):
            for j in range(cols):
                 value=matrix1[i][j]
                 if j > i and  value%2==0:
                     c+=1
                     t.append(value)
                     print("%",value,end=" ")  
        print("Even Number Above Main Diagonal",c)
        print(tuple(t))
    case 2:
        row=int(input("Enter number of rows="))
        cols=int(input("Enter number of columns="))
        print("Enter elements of matrix A")
        matrix1=[]
        for i in range(row):
         rows=[]
         for j in range(cols):
            rows.append(int(input()))
         matrix1.append(rows)
        print("Enter Matrix ")
        for rows in matrix1:
            for val in rows:
                 print(val,end=" ")
            print()
        c=0
        t=[]
        for i in range(row):
            for j in range(cols):
                value=matrix1[i][j]
                if i>j and value%2!=0:
                     c+=1
                     t.append(value)
                   
        print("Odd Number Above main Diagonal",c)
        print(tuple(t))

    case 3:    
        row=int(input("Enter number of rows="))
        cols=int(input("Enter number of columns="))
        print("Enter elements of matrix A")
        matrix1=[]
        for i in range(row):
         rows=[]
         for j in range(cols):
            rows.append(int(input()))
         matrix1.append(rows)
        print("Enter Matrix ")
        for rows in matrix1:
            for val in rows:
                 print(val,end=" ")
            print()   
           

        

