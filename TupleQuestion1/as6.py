'''Read N product details from the user and store them as tuples in a list.
Display all product details.
Find and display the costliest product.
Find and display the cheapest product.
Calculate and display the average price of all products.
Display all products whose price is greater than ₹50,000.

Test Case:

Input:

Enter number of products: 4

P101 Laptop 65000
P102 Mobile 25000
P103 Television 80000
P104 Tablet 30000

Expected Output:

All Products:
('P101', 'Laptop', 65000)
('P102', 'Mobile', 25000)
('P103', 'Television', 80000)
('P104', 'Tablet', 30000)

Costliest Product:
('P103', 'Television', 80000)

Cheapest Product:
('P102', 'Mobile', 25000)

Average Price:
50000.0

Products Above ₹50,000:
('P101', 'Laptop', 65000)
('P103', 'Television', 80000)'''



from collections import namedtuple
Product=namedtuple("prod",["product_id", "product_name", "price"])
n=int(input("Enter number of products:"))

product=[]
for i in range(n):
   print("Enter Details:")
   id=input("Enter the id of product:")
   name=input("Enter the product name:")
   price=int(input("Enter the price of product:"))
   pr=Product(id,name,price)
   product.append(pr)

costliest=None
cheapest=None
for x in product:
    print(x.product_id,x.product_name,x.price)
sums=0
Avg=0

for x in product:
    print(x)
    sums+=x.price
costliest=None
cheapest=None
if costliest==None or x.price>costliest:
   costliest=x
if cheapest==None or x.price<cheapest:
   cheapest=x
Avg=sums/n

print("Costliest Product:")
print(x.product_id,x.product_name,x.price)


print("Cheapest Product:")
print(x.product_id,x.product_name,x.price)

print("Average price:")
print(Avg)

for x in product:
    if x.price>50000:
       print(x.product_id,x.product_name,x.price)




   



   
   



