'''Assignment 4: Travel Distance Calculation

A person is traveling at a constant speed. Time is given in hours and minutes. Convert total time into hours and calculate distance.

Input:
Speed = 60 km/hr
Time = 2 hours 30 minutes

Expected Output:
Total Time = 2.5 hours
Distance = 150.0 km'''



speed=int(input("Speed="))
time_hrs,time_min=map(int,input("Time=").split())
total_time=time_hrs+time_min/60
distance=speed*total_time
print(f"Total Time={total_time}\n Distance={distance}")
