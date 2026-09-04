'''
3.
ONLINE SHOPPING SYSTEM

Scenario:

An e-commerce company wants to develop an Online Shopping System.
 The application should be menu-driven and should demonstrate different types of arguments used in Python functions.

MENU

1. Customer Registration
2. Product Information
3. Generate Invoice
4. Add Multiple Products
5. Display Customer Profile
6. Exit

Requirements

Choice 1 – Customer Registration

* Accept Customer Name, Email, and Mobile Number.
* Pass the values to a function using Positional Arguments.
* Display the registered customer details.

Choice 2 – Product Information

* Accept Product Name, Price, and Category.
* Call the function using Keyword Arguments.
* Display the product details.

Choice 3 – Generate Invoice

* Accept Product Name and Price.
* Tax Percentage should have a default value.
* Use Default Arguments while generating the invoice.
* Display the final amount.

Choice 4 – Add Multiple Products

* Allow the user to enter any number of product prices.
* Pass all prices to a function using Variable Length Arguments (*args).
* Calculate and display the total bill amount.

Choice 5 – Display Customer Profile

* Accept any number of customer details such as Name, City, Email, Mobile, Membership Type, etc.
* Pass the details using Arbitrary Keyword Arguments (**kwargs).
* Display all customer information.

Choice 6 – Exit

Sample Execution

Enter Choice : 1

Enter Name : Ajay
Enter Email : [ajay@gmail.com](mailto:ajay@gmail.com)
Enter Mobile : 9876543210

Customer Registered Successfully

---

Enter Choice : 2

Enter Product Name : Laptop
Enter Price : 55000
Enter Category : Electronics

Product Details Displayed Successfully

---

Enter Choice : 3

Enter Product Name : Laptop
Enter Price : 55000

Invoice Generated Successfully

---

Enter Choice : 4

Enter Number of Products : 4

Enter Price 1 : 100
Enter Price 2 : 200
Enter Price 3 : 300
Enter Price 4 : 400

Total Bill Amount : 1000

---

Enter Choice : 5

Customer Profile Displayed Successfully

---

Enter Choice : 6

Thank You. Program Terminated.

Important Instructions

1. Choice 1 must use Positional Arguments.
2. Choice 2 must use Keyword Arguments.
3. Choice 3 must use Default Arguments.
4. Choice 4 must use Variable Length Arguments (*args).
5. Choice 5 must use Arbitrary Keyword Arguments (**kwargs).
6. Use separate functions for each menu option.
7. Implement the solution using a menu-driven approach.
8. Maintain proper code readability and formatting.

Note:
Marks will be awarded based on the correct usage of the specified argument type in each menu option.'''


def Registration(name,email,mobile_no):
    print("Customer Registered Successfully")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Mobile_no:{mobile_no}")
def product(product,price,category):
    print("product details added successfully")
    print(f"product :{product}")
    print(f"price :{price}")
    print(f"category:{category}")
def invoice(product,price,tax=5):
    tax_count=(price*tax)/100
    final=tax_count+price
    print("Invoice generated successfully")
    print(f"Product: {product}")
    print(f"Price: {price}")
    print(f"Tax: {tax}%")
    print(f"Final Amount: {final}")
def multiple_product(*args):
    total = 0

    for price in args:
        total += price

    return total
def customer_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


while True:
 print("MENU")
 print("1. Customer Registration")
 print("2. Product Information")
 print("3. Generate Invoice")
 print("4. Add Multiple Products")
 print("5. Display Customer Profile")
 print("6. Exit")
 choice=int(input("Enter your choice;"))
 match choice:
  case 1:
       name=input("Enter the name: ")
       email=input("Enter the Email: ")
       mobile_no=input("Enter the Mobile number:")
       #positional argument
       print(Registration(name,email,mobile_no))
  case 2:
       product=input("enter the product ")
       price=int(input("enter the price of product: "))
       category=input("enter the category of product: ")
       #keyword argument
       print(product(product=product,price=price,category=category))
  case 3:
       product=input("Enter the product: ")
       price=int(input("Enter the product of price: "))
       #default parameter
       print(invoice(product,price))
  case 4:
        n=int(input("Enter the number of products:"))
        price=[]


        for i in range(n):
            price = int(input(f"Enter Price {i+1}: "))
            price.append(price)

            # Variable Length Arguments (*args)
            total = multiple_product(*price)
            print("Total Bill Amount:", total)
  case 5:
         name=input("Enter the name of the customer:")
         email=input("Enter the Email of the customer: ")
         mobile_no=input("Enter the Mobile of the customer: ")
         p_name=input("Enter the product name: ")
         p_price=int(input("Enter the price of product:"))
         customer_profile(name=name,email=email,mobile_no=mobile_no,product=p_name,price=p_price)
  case 6:
          print("Existing----------")      
  case __:
         print("Invalid choice")