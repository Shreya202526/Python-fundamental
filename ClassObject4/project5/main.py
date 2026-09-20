from model.book import Book  


n=int(input("Enter the number of books:"))
books=[]
for i in range(n):
    book_id=int(input("Enter the book_id:"))
    book_name=input("Enter Book name:")
    author=input("Enter Author Name:")
    price=int(input("Enter the price of books "))
    book=Book(book_id,book_name,author,price)
    books.append(book)

print("All Books")
for book in books:
    print(book.book_id,book.book_name,book.author,book.price)

search_id=int(input("Enter Book_ID:"))
found=False
for book in books:
    if book.book_id==search_id:
        print("Book Found:")
        print(book.book_id,book.book_name,book.author,book.price)
        found=True
        break
if not found:
    print("Book Not Found")



author_name=int(input("Enter Author Name:"))
print(f"Books by {author_name}")
for book in books:
    if book.author.lower()==author_name.lower():
        print(book.book_id,book.book_name,book.author,book.price)
    else:
        print("Book Not found")

print("Books with price greater than 500:")
for book in books:
     if book.price > 500:
         print(book.book_id,book.book_name,book.author,book.price)



highest=0
highest_student=None
print("Most Expensive Book:")
for book in books:
    if book.marks>highest:
        highest=book.marks
        highest_book=book
print(highest_book.book_id,highest_book.book_name,highest_book.author,highest_book.price)

print("Average:-")
sum=0
for boook in books:
    sum+=book.price
avg=sum/n
print(avg)



