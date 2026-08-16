'''4.

=========================================================
        MATRIX DIAGONAL ANALYSIS SYSTEM
=========================================================

Scenario

A security company stores surveillance data in matrix form.
The analyst wants a menu-driven application to examine the
diagonal elements of the matrix and generate reports.

The application should allow the user to:

1. Display Main Diagonal Elements
2. Display Secondary Diagonal Elements
3. Compare Main and Secondary Diagonal Sums
4. Exit

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user selects Exit.

   1. Display Main Diagonal Elements
   2. Display Secondary Diagonal Elements
   3. Compare Main and Secondary Diagonal Sums
   4. Exit

2. Read the size of a square matrix from the user.

3. Read all matrix elements from the user.

4. Based on the user's choice:

   Choice 1 - Display Main Diagonal Elements
   -----------------------------------------
   Display all elements present in the main diagonal.

5. Choice 2 - Display Secondary Diagonal Elements
   ----------------------------------------------
   Display all elements present in the secondary diagonal.

6. Choice 3 - Compare Main and Secondary Diagonal Sums
   ---------------------------------------------------
   Calculate the sum of both diagonals and display:

   - Main Diagonal Sum
   - Secondary Diagonal Sum
   - Which diagonal has the greater sum
   - Or whether both sums are equal

7. Choice 4 - Exit
   -----------------------------------------
   Display:
   "Thank You for Using Matrix Diagonal Analysis System"

---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------

Enter size of matrix: 3

Enter matrix elements:

1 2 3
4 5 6
7 8 9

Menu
1. Display Main Diagonal Elements
2. Display Secondary Diagonal Elements
3. Compare Main and Secondary Diagonal Sums
4. Exit

Enter your choice: 1

Output:
Main Diagonal Elements:
1 5 9

---------------------------------------------------------

Enter your choice: 2

Output:
Secondary Diagonal Elements:
3 5 7

---------------------------------------------------------

Enter your choice: 3

Output:
Main Diagonal Sum = 15
Secondary Diagonal Sum = 15
Both Diagonal Sums are Equal

========================================================='''


print("Menu")
print("1. Display Main Diagonal Elements")
print("2. Display Secondary Diagonal Elements")
print("3. Compare Main and Secondary Diagonal Sums")
print("4. Exit")
choice=int(input("Enter your choice:"))
match choice:
    case 1:

      row=int(input("Enter number of rows="))
      cols=int(input("Enter number of columns="))
      print("Enter elements of matrix ")
      matrix1=[]
      for i in range(row):
       rows=[]
       for j in range(cols):
        rows.append(int(input()))
       matrix1.append(rows)
      print("Main Diagonal are=")
      for i in range(row):
       for j in range(cols):
          if i==j:
           print(matrix1[i][j],end=" ")
    case 2:

      row=int(input("Enter number of rows="))
      cols=int(input("Enter number of columns="))
      print("Enter elements of matrix ")
      matrix1=[]
      for i in range(row):
       rows=[]
       for j in range(cols):
        rows.append(int(input()))
       matrix1.append(rows)
      print("Main Diagonal are=")
      for i in range(row):
       for j in range(cols):
          if j==cols-1-i:
           print(matrix1[i][j],end=" ")
    case 3:
         row=int(input("Enter number of rows="))
         cols=int(input("Enter number of columns="))
         print("Enter elements of matrix ")
         matrix1=[]
         for i in range(row):
            rows=[]
            for j in range(cols):
             rows.append(int(input()))
            matrix1.append(rows)
         print("Main Diagonal are=")
         sums1=0
         for i in range(row):
            for j in range(cols):
               value=matrix1[i][j]
               if i==j:
                sums1+=value
                print(value)  
         print("Main Diagonal sum is",sums1)  
         print("Secondary Diagonal are=")
         sums2=0
         for i in range(row):
          for j in range(cols):
               val=matrix1[i][j]
               if j==cols-1-i:
                  sums2+=val
                  print(val)
         print("Secondary sum of diagonal",sums2)
         if sums1==sums2:
           print("Both diagonals sum are equal")
         else:
           print("Both diagonal sum are not equal")
    case 4:
              print("Thank You for Using Matrix Quality Check System")
    case __:
             print("Invalid output")
         
        
