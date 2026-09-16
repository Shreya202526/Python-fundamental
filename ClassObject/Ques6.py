'''Assignment 6: Electricity Bill Calculator

An electricity board wants to calculate a customer's electricity bill based on units consumed.

Create a class ElectricityBill with the following attributes:

Consumer number

Consumer name

Units consumed

Rate per unit

Fixed charge

Create the following methods:

calculate_energy_charge() – Calculate units × rate per unit.

calculate_total_bill() – Add energy charge and fixed charge.

display_bill() – Display consumer details and bill amount.

Sample data:

Consumer Number: 501
Consumer Name: Amit
Units Consumed: 250
Rate Per Unit: 6
Fixed Charge: 100

Expected result:

Energy Charge: 1500
Total Bill: 1600'''



class ElectricityBill:
    def set(self,c_num,c_name,units,rate,fixed_c):
        self.c_num=c_num
        self.c_name=c_name
        self.units=units
        self.rate=rate
        self.fixed_c=fixed_c

    def calculate_energy_charge(self):
        self.energy=self.units*self.rate

    def total_bill(self):
        self.total=self.energy+self.fixed_c

    def display_bill(self):
        print("Consumer Number: ",self.c_num)
        print("Consumer Name: ",self.c_num)
        print("Units Consumed:", self.units)
        print("Rate Per Unit: ",self.rate)
        print("Fixed Charge:", self.fixed_c)
        print()
        print("Energy Charges:",self.energy)
        print("Total Charge:",self.total)

c1=ElectricityBill()
c1.set(501,"Amit",250,6,100)
c1.calculate_energy_charge()
c1.total_bill()
c1.display_bill()
