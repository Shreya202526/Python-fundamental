'''=====================================================================
QUESTION 5: LIBRARY BOOK RECORDS
================================

A library maintains book information using NamedTuple.

Fields:
book_id, title, author, price

Requirements:

1. Read N book records from the user and store them in a list of NamedTuples.

---

2. Display all book details.

---

3. Find and display the most expensive book.

---

4. Search books by author name.

---

5. Calculate and display the average price of all books.

---

Test Case:

Input:
Enter number of books: 4

B101 Python Basics John 450
B102 Java Programming James 550
B103 Data Science John 700
B104 SQL Guide Smith 300

Enter Author Name: John

Expected Output:
Most Expensive Book:
B103 Data Science John 700

Average Book Price:
500.0

Books Written By John:
B101 Python Basics John 450
B103 Data Science John 700'''

from collections import namedtuple
Books=namedtuple("book",["book_id","title","author","price"])
n=int(input("Enter the number of books"))
books=[]
for i in range(n):
    print("Details")
    id=input("Enter the Order Id=")
    title=input("Enter the Title name=")
    author=input("Enter the Author name =")
    price = int(input("Enter the price="))
    book= Books(id,title,author,price)
    books.append(book)
for x in books:
    print(x.book_id,x.title,x.author,x.price)
print()
author_name=input("Enter Author name:")
max_book=None
sums=0
for x in books:
    if max_book==None or x.price>max_book:
        max_book=x
    if author_name==x.author:
        print()
        print(x.book_id,x.title,x.author,x.price)
avg=sums/n
print("Average book price",avg)
print()
if x.author==author_name:
   print(x.book_id,x.title,x.author,x.price)