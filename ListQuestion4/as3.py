'''.

=========================================================
         MATRIX QUALITY CHECK SYSTEM
=========================================================

Scenario

A manufacturing company records quality inspection values in
matrix form. The Quality Control team wants a menu-driven
application to analyze the inspection data and generate reports.

The application should allow the user to:

1. Count Armstrong Numbers Row-wise
2. Count Palindrome Numbers Column-wise
3. Display Average of Each Row
4. Exit

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user selects Exit.

   1. Count Armstrong Numbers Row-wise
   2. Count Palindrome Numbers Column-wise
   3. Display Average of Each Row
   4. Exit

2. Read the number of rows and columns from the user.

3. Read all matrix elements from the user.

4. Based on the user's choice:

   Choice 1 - Count Armstrong Numbers Row-wise
   -------------------------------------------
   Count and display the number of Armstrong numbers
   present in each row.

   Examples:
   153, 370, 371, 407

5. Choice 2 - Count Palindrome Numbers Column-wise
   -----------------------------------------------
   Count and display the number of palindrome numbers
   present in each column.

   Examples:
   121, 131, 444, 1221

6. Choice 3 - Display Average of Each Row
   --------------------------------------
   Calculate and display the average of each row.

7. Choice 4 - Exit
   --------------------------------------
   Display:
   "Thank You for Using Matrix Quality Check System"

---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------

Menu
1. Count Armstrong Numbers Row-wise
2. Count Palindrome Numbers Column-wise
3. Display Average of Each Row
4. Exit

Enter your choice: 1

Enter rows: 3
Enter columns: 3

Enter matrix elements:
153 121 10
370 22 44
407 15 131

Output:
Row 1 Armstrong Count = 1
Row 2 Armstrong Count = 1
Row 3 Armstrong Count = 1

---------------------------------------------------------

Enter your choice: 2

Output:
Column 1 Palindrome Count = 0
Column 2 Palindrome Count = 3
Column 3 Palindrome Count = 2
'''
print("Menu")
print("1. Count Armstrong Numbers Row-wise")
print("2. Count Palindrome Numbers Column-wise")
print("3. Display Average of Each Row")
print("4. Exit")
choice=int(input("Enter your choice:"))
match choice:
    case 1:
        r=int(input("Enter number of rows="))
        c=int(input("Enter number of columns="))
        print("Enter elements of matrix ")
        matrix1=[]
        for i in range(r):
            rows=[]
            for j in range(c):
               rows.append(int(input()))
            matrix1.append(rows)

        for row in range(0,r):
            count=0
            for val in range(c):
             value=matrix1[row][val]
             real=value
             sums=0
             pow=len(str(value))
             
             while value>0:
                d=value%10
                sums=sums+d**pow
                value=value//10

             if sums==real:
               count+=1
               print("Row=",row+1,"armstrong ",count,"count",real)
    case 2:
        r=int(input("Enter number of rows="))
        c=int(input("Enter number of columns="))
        print("Enter elements of matrix ")
        matrix1=[]
        for i in range(r):
            rows=[]
            for j in range(c):
               rows.append(int(input()))
            matrix1.append(rows)

        for row in range(0,r):
            count=0
            for val in range(c):
             value=matrix1[row][val]
             real=value
             rev=0
             pow=len(str(value))
             
             while value>0:
                d=value%10
                rev=rev*10+d
                value=value//10

             if rev==real:
               count+=1
               print("Row=",row+1,"pallindrome= ",count,"count",real)
    case 3:
        r=int(input("Enter number of rows="))
        c=int(input("Enter number of columns="))
        print("Enter elements of matrix ")
        matrix1=[]
        for i in range(r):
            rows=[]
            for j in range(c):
               rows.append(int(input()))
            matrix1.append(rows)
        
        for row in matrix1:
            sums=0
            for val in row:
               sums+=val
               avg=sums/c
            print(avg)
    case 4:
       print("Thank You for Using Matrix Quality Check System")
    case __:
      print("Invalid output")

         

                
            