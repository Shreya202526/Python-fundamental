'''============================================================

ASSIGNMENT 3 — VEHICLE RENTAL SYSTEM
====================================


A vehicle rental company rents different types of vehicles.

Create:

Vehicle
|
+-------- Car
|
+-------- Bike

REQUIREMENTS:

1. Create Vehicle class.

Attributes:

* vehicle_number
* brand
* rent_per_day

2. Car should inherit from Vehicle.

Additional:

* number_of_seats

3. Bike should inherit from Vehicle.

Additional:

* engine_cc

4. Initialize parent data using super().

5. Create:

display_vehicle()
calculate_rent(days)

6. Override calculate_rent() in Car and Bike.

7. The child methods must call the parent calculation using super().

8. Use a property for rent_per_day.

9. Create:

@property
@rent_per_day.setter
@rent_per_day.deleter

10. rent_per_day must be greater than 0.

11. Read all information from the user.

INPUT:

Enter Vehicle Number:
Enter Brand:
Enter Rent Per Day:
Enter Vehicle Type:

1. Car
2. Bike

If Car:

Enter Number of Seats:

If Bike:

Enter Engine CC:

Enter Number of Rental Days:

SAMPLE INPUT:

Enter Vehicle Number: MP09AB1234
Enter Brand: Hyundai
Enter Rent Per Day: 1500
Enter Vehicle Type: 1
Enter Number of Seats: 5
Enter Number of Rental Days: 4

EXPECTED OUTPUT:

## Vehicle Details

Vehicle Number: MP09AB1234
Brand: Hyundai
Rent Per Day: 1500
Vehicle Type: Car
Number of Seats: 5

Rental Days: 4
Total Rent: 6000'''

class Vehicle:
    def _init_(self,vehicle_number,brand,rent_per_day):
        self.vehicle_number=vehicle_number
        self.brand=brand
        self.rent_per_day=rent_per_day
    @property
    def rent_per_day(self):
        return self.__rent_per_day
    @rent_per_day.setter
    def rent_per_day(self,new):
        if new<0:
            raise ValueError("Salary must be greater than 0")
        self.__rent_per_day=new
    @rent_per_day.deleter
    def rent_per_day(self):
        print("Deleting the rent per day")
        del self.__rent_per_day
    def display_vehicle(self):
        print("Vehicle number:",self.vehicle_number)
        print("Brand:",self.brand)
        print("Rent per day:",self.rent_per_day)


class Car(Vehicle):
    def _init_(self,vehicle_number,brand,rent_per_day,number_of_seats):
        super()._init_(vehicle_number,brand,rent_per_day)
        self.number_of_seats=number_of_seats
    def display_vehicle(self):
        super().display_vehicle()
class Bike(Vehicle):
    def _init_(self,vehicle_number,brand,rent_per_day,engine_cc):
        super()._init_(vehicle_number,brand,rent_per_day)
        self.engine_cc=engine_cc
    def display_vehicle(self):
        super().display_vehicle()
        
vno=int(input("Enter Vehicle Number:"))
brand=input("Enter Brand:")
rent=int(input("Enter Rent Per Day:"))
type=input("Enter Vehicle Type:(Car/Bike)")
if type=="Car":
    seats=int(input("Enter no. of seats:"))
    vehicle=Car(vno,brand,rent,seats)
elif type=="Bike":
    cc=int(input("Enter Engine CC:"))
    rental=int(input("Enter Number of Rental Days:"))
    vehicle=Bike(vno,brand,rent,cc)
vehicle.display_vehicle()