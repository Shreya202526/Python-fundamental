from model.customer import Customer
n=int(input("Enter the number of Customer:"))
customers=[]
for i in range(n):
    customer_id=int(input("Enter Cutomer ID:"))
    customer_name=input("Enter Customer name:")
    city=input("Enter City:")
    purchase_amount=int(input("Enter Purchase Amount:"))
    customer=Customer(customer_id,customer_name,city,purchase_amount)
    customers.append(customer)

print("All Customer:")
for customer in customers:
    print(customer.customer_id,customer.customer_name,customer.city,customer.purchase_amount)



city=input("Enter the city:")
print(f"Customers from {city}:")
for customer in customer:
    if customer.city==city:
        print(customer.customer_id,customer.customer_name,customer.city,customer.purchase_amount)



print("Customers with purchase amount greater than 10000:")
for customer in customers:
    if customer.purchase_amount>10000:
        print(customer.customer_id,customer.customer_name,customer.city,customer.purchase_amount)


highest=0
highest_p=None
print("Highest Purchase Customer")
for customer in customers:
          if customer.purchase_amount>highest:
              highest=customer.purchase_amount
              highest_p=customer
print(highest_p.customer_id,highest_p.customer_name,highest_p.city,highest_p.purchase_amount)


print("Total sales:")
sum=0
for customer in customers:
    sum+=customer.purchase_amount
avg=sum/n
print(sum)
print("Average sales:")
print(avg)


customer_id=int(input("Customer ID:"))
found=False
for customer in customers:
    if customer.customer_id==customer_id:
        print("Customer Found:")
        print(highest_p.customer_id,highest_p.customer_name,highest_p.city,highest_p.purchase_amount)
        found=True
        break
if not found:
    print("Customer Not Found")