from model.product import Product

products=[]
n=int(input("Enter the number of product:"))
for i in range(n):
   product_id=int(input("Enter the product id:"))
   product_name=input("Enter the product name:")
   price=int(input("Enter the price:"))
   quantity=int(input("Enter the Quantity:"))
   p1=Product(product_id,product_name,price,quantity)
   products.append(p1)

def display_products(products):
    print("All products:")

    for product in products:
        print(product.product_id,product.product_name,product.price,product.quantity)
    return product



def display_productsvalue(products):
    print("Product Total Values")
    for product in products:
        print(f"{product.product_name}={product.price*quantity}")




def display_highest(products):
    highest=0
    highest_product=None
    print("Highest product")
    for product in products:
          if product.price>highest:
              highest=product.price
              highest_product=product
    print(highest_product.product_id,highest_product.product_name,highest_product.price,highest_product.quantity)
display_highest(products)


def display_lowstock(products):
    print("Low Stock product")
    for product in products:
          if product.quantity< 10:
              print(product.product_name)



def search_product(products, search_id):
    for product in products:
        if product.product_id == search_id:
            print("\nProduct Found:")
            print(product.product_id, product.product_name,
                  product.price, product.quantity)
            return

    print("Product not found")
search_id=int(input("Enter product:"))
search_product(products, search_id)


def display_inventory(products):
    total=0
    total_i=0
    for product in products:
        total=product.quantity*product.price
        total_i+=total
    print("\nTotal Inventory Value:")
    print(total_i)



display_products(products)
display_productsvalue(products)
display_lowstock(products)
display_highest(products)

display_inventory(products)

search_id=int(input("Enter product:"))
search_product(products, search_id)
