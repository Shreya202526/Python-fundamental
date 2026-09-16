'''Assignment 8: Car Mileage Calculator

 A car owner wants to calculate the mileage and fuel cost of a journey.

Create a class Car with the following attributes:

Car brand

Car model

Distance travelled in km

Fuel consumed in litres

Petrol price per litre

Create the following methods:

calculate_mileage() – Calculate kilometres per litre.

calculate_fuel_cost() – Calculate total fuel cost.

display_trip_details() – Display car and journey details.

Formulas:

Mileage = Distance / Fuel Consumed
Fuel Cost = Fuel Consumed × Petrol Price

Sample data:

Car Brand: Maruti
Car Model: Swift
Distance: 320 km
Fuel Consumed: 20 litres
Petrol Price: 105
'''

class Car:
    def set(self,brand,model,distance,fuel,petrol_p):
        self.brand=brand
        self.model=model
        self.distance=distance
        self.fuel=fuel
        self.petrol=petrol_p

    def calculate_mileage(self):
        self.mileage=self.distance/self.fuel

    def calculate_fuel_cost(self):
        self.fuel_cost=self.mileage*self.petrol

    def display_trip_details(self):
        print("Car Brand:", self.brand)
        print("Car Model:", self.model)
        print("Distance Travelled:", self.distance, "km")
        print("Fuel Consumed:", self.fuel, "litres")
        print("Petrol Price:", self.petrol)
        print("Mileage:", self.mileage, "km/l")
        print("Fuel Cost:", self.fuel_cost)

c1=Car()
c1.set("Maruti","Swift",320,20,105)
c1.calculate_mileage()
c1.calculate_fuel_cost()
c1.display_trip_details()