'''Question 3: Online Shopping System
Scenario

An e-commerce company wants to calculate the final amount payable by customers after applying discounts.

Requirements

Create a class named Product with:

product_id
product_name
quantity
price_per_item

Initialize the values using a constructor.

Calculations
Total Amount = Quantity × Price Per Item
If Total Amount > ₹5000, Discount = 10%
Otherwise, Discount = 5%
Final Amount = Total Amount − Discount
Sample Input
Enter Product ID : P101
Enter Product Name : Laptop
Enter Quantity : 2
Enter Price Per Item : 35000
Sample Output
------ Shopping Bill ------
Product ID        : P101
Product Name      : Laptop
Quantity          : 2
Price Per Item    : 35000.0
Total Amount      : ₹70000.0
Discount          : ₹7000.0
Final Amount      : ₹63000.0'''


class Product:
    def __init__(self,product_id,product_name,quantity,price_per_item):
        self.product_id=product_id
        self.product_name=product_name
        self.quantity=quantity
        self.price_per_item=price_per_item
    def calculate_total_amt(self):
        self.total=self.quantity*self.price_per_item

    def calculate_discount(self):
        if self.total>5000:
            self.discount=(10/100)*self.total
        else:
            self.discount=(5/100)*self.total

    def final_amt(self):
        self.final=self.total-self.discount

    def display_details(self):
        print("--------Shopping Bill----------")
        print("Product ID     :",self.product_id)
        print("Product Name   :",self.product_name)
        print("Quantity       :",self.quantity)
        print("Price Per Item :",self.price_per_item)
        print("Total Amount   :",self.total)
        print("Discount       :",self.discount)
        print("Final Amount   :",self.final)


product_id=input("Enter Product ID :")
product_name=input("Enter Product Name :")
quantity=int(input("Enter Quantity: "))
price_per_item=int(input("Enter Price Per Item: "))

p1=Product(product_id,product_name,quantity,price_per_item)
p1.calculate_total_amt()
p1.calculate_discount()
p1.final_amt()
p1.display_details()