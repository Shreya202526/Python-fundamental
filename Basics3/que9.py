'''Assignment 9: Petrol Cost Calculation

You traveled a certain distance. Based on mileage and petrol price, calculate fuel used and total cost.

Input:
Distance = 450 km
Mileage = 15 km/litre
Petrol price = 110/litre

Expected Output:
Petrol Used = 30.0 litres
Total Cost = 3300.0'''

distance=int(input("Distance="))
mileage=int(input("Mileage="))
pp=int(input("Petrol price="))

petrol_used=distance/mileage
total_cost=pp*petrol_used
print(f" Petrol Used={petrol_used} litres\n Total Cost={total_cost}")



