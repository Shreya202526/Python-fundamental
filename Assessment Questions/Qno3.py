'''QUESTION 3: LIBRARY BOOK RECORD ANALYSIS(3 marks)

A library wants to maintain and analyze its book records using NamedTuple.

Each book contains the following information:

Fields:
book_id, title, author, price

Requirements:
Read N book records from the user and store them in a list of NamedTuple.
Display all book details.
Find and display the most expensive book.
Find and display the cheapest book.
Calculate and display the average price of all books.
Display all books whose price is greater than the average book price.
Test Case

Input:

Enter number of books: 6

Enter details for Book 1:
Enter Book ID: B201
Enter Title: C Programming
Enter Author: Robert
Enter Price: 400

Enter details for Book 2:
Enter Book ID: B202
Enter Title: Web Development
Enter Author: Martin
Enter Price: 650

Enter details for Book 3:
Enter Book ID: B203
Enter Title: Python Advanced
Enter Author: Robert
Enter Price: 800

Enter details for Book 4:
Enter Book ID: B204
Enter Title: Database Systems
Enter Author: Thomas
Enter Price: 500

Enter details for Book 5:
Enter Book ID: B205
Enter Title: Machine Learning
Enter Author: David
Enter Price: 900

Enter details for Book 6:




Enter Book ID: B206
Enter Title: Computer Networks
Enter Author: Martin
Enter Price: 350
Expected Output
All Book Details:
B201 C Programming Robert 400
B202 Web Development Martin 650
B203 Python Advanced Robert 800
B204 Database Systems Thomas 500
B205 Machine Learning David 900
B206 Computer Networks Martin 350

Most Expensive Book:
B205 Machine Learning David 900

Cheapest Book:
B206 Computer Networks Martin 350

Average Book Price:
600.0

Books With Price Greater Than Average:
B202 Web Development Martin 650
B203 Python Advanced Robert 800
B205 Machine Learning David 900'''



from collections import namedtuple
n=int(input("Enter the number of books:"))

Book=namedtuple("book",["book_id", "title", "author", "price"])
Books=[]
for i in range(n):
      id=int(input("Enter the id of books:"))
      title=input("Enter the title of the books:")
      author=input("Enter the author of the books:")
      price=int(input("Enter the price of the books:"))
      b=Book(id,title,author,price)
      Books.append(b)
print(Books)
exp=None
sums=0
cheap=None
print("All Book details")
for x in Books:
      print(x.book_id,x.title,x.author,x.price)

for x in Books: 
  sums+=x.price
  if exp is None or x.price>exp.price:
      exp=x
      
  if cheap is None or x.price<cheap.price:
      cheap=x

      
avg=sums/n
print("Average:",avg)

print(exp)
print(cheap)



