'''5.
=========================================
LIBRARY ISBN MANAGER
=========================================

A library stores unique ISBN numbers of books.

Menu:
1. Add ISBN
2. Remove ISBN
3. Search ISBN
4. Display ISBN List
5. Count Books
6. Exit

Requirements:
- Use Set.
- Duplicate ISBNs are not allowed.'''

isbn_set=set()

while True:
   print("Menu:")
   print("1. Add ISBN")
   print("2. Remove ISBN")
   print("3. Search ISBN")
   print("4. Display ISBN List")
   print("5. Count Books")
   print("6. Exit")
   choice=int(input("Enter your choice:"))
   match choice:
         case 1:
               isbn=int(input("Enter isbn:"))
               if isbn  in isbn_set:
                  print("isbn is already exists:")
               else:
                  isbn_set.add(isbn)
                  print("isbn added successfully")
         case 2:
               isbn=int(input("Enter isbn:"))
               if isbn  not in isbn_set:
                  print("isbn is not exists:")
               else:
                  isbn_set.remove(isbn)
                  print("isbn remove successfully")

         case 3:
               isbn=input("Enter ISBN to search: ")
               if isbn in isbn_set:
                print("ISBN found.")
               else:
                print("ISBN not found.")

         case 4:
            if isbn_set:
                print("ISBN List:", isbn_set)
            else:
                print("No ISBNs available.")

         case 5:
            print("Total Books:", len(isbn_set))

         case 6:
            print("Exiting Library ISBN Manager...")
            break

         case _:
            print("Invalid choice! Please try again.")


