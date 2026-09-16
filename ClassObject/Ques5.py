'''Assignment 5: Shopping Bill Calculator

 A retail shop wants to calculate the total bill for a customer.

Create a class ShoppingBill with the following attributes:

Product name

Product price

Quantity

Discount percentage

GST percentage

Create the following methods:

calculate_subtotal() – Calculate price × quantity.

calculate_discount() – Calculate the discount amount.

calculate_gst() – Calculate GST on the discounted amount.

calculate_final_bill() – Calculate the final payable amount.

display_bill() – Display the complete bill details.

Formula:

Subtotal = Price × Quantity
Discounted Amount = Subtotal - Discount
GST = Discounted Amount × GST Percentage / 100
Final Bill = Discounted Amount + GST'''


class ShoppingBill:
    def set(self,pname,pp,quantity,dis_p,gst):
        self.pname=pname
        self.pp=pp
        self.quantity=quantity
        self.dis_p=dis_p
        self.gst=gst

    def calculate_subtotal(self):
        self.subtotal=self.pp*self.quantity

    def calculate_discount(self):
        self.discount=self.subtotal*(self.dis_p / 100)
        self.after_discount = self.subtotal - self.discount

    def calculate_gst(self):
        self.gst_p=self.after_discount*(self.gst/100)

    def calculate_final_bill(self):
        self.bill=self.after_discount+self.gst_p

    def display_bill(self):
        print("Product Name:", self.pname)
        print("Price:", self.pp)
        print("Quantity:", self.quantity)
        print("Subtotal:", self.subtotal)
        print("Discount:", self.discount)
        print("GST:", self.gst_p)
        print("Final Bill:", self.bill)



c1=ShoppingBill()
c1.set("laptop",50000,2,5,2)
c1.calculate_subtotal()
c1.calculate_discount()
c1.calculate_gst()
c1.calculate_final_bill()
c1.display_bill()