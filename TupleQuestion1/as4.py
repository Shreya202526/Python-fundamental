'''=====================================================================
QUESTION 4: ONLINE SHOPPING ORDERS
==================================

An online shopping company stores customer orders using NamedTuple.

Fields:
order_id, customer_name, product_name, amount

Requirements:

1. Read N order records from the user and store them in a list of NamedTuples.

---

2. Display all order details.

---

3. Find and display the order having the highest amount.

---

4. Calculate and display total sales.

---

5. Count the number of orders whose amount is greater than ₹10,000.

---

Test Case:

Input:
Enter number of orders: 5

O101 Rahul Laptop 55000
O102 Priya Mouse 800
O103 Amit Mobile 25000
O104 Neha Keyboard 1500
O105 Rakesh TV 45000

Expected Output:
Highest Value Order:
O101 Rahul Laptop 55000

Total Sales:
127300

Orders Above ₹10,000:
3'''



from collections import namedtuple
Order=namedtuple("order",["order_id","customer_name","product_name","amount"])
n=int(input("Enter the number of orders"))
order=[]
for i in range(n):
    print("Details")
    id=input("Enter the Order Id=")
    name=input("Enter the Customer name=")
    prod=input("Enter the product name =")
    amount = int(input("Enter the amount="))
    orders= Order(id,name,prod,amount)
    order.append(orders)
max_order=None
sales=0
order_count=0
for x in order:
    sales+=x.amount
    print(x.order_id,x.customer_name,x.product_name,x.amount)
    if max_order==None or x.amount>max_order:
        max_order=x
    if x.amount>10000:
        order_count+=1
print()
print("Highest Value Order")
print(x.order_id,x.customer_name,x.product_name,x.amount)

print()
print("Total sales")
print(sales)
print()
print("Order Above 10000:")
print(order_count)


