'''Assignment 10: Time Conversion

Convert total seconds into hours, minutes, and seconds.

Input:
Total seconds = 7384

Expected Output:
Hours = 2
Minutes = 3
Seconds = 4'''


total_seconds=int(input("Total Seconds="))
hrs=total_seconds//3600
remaining=total_seconds%3600
min=remaining//60
sec= remaining%60
print(f"Hours={hrs}\n Minutes={min}\n Seconds={sec}")


