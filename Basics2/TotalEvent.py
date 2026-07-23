'''An event management company is developing a scheduling system. One of the key tasks is converting the duration of events from total seconds (which their sensor system records) into a more human-readable format of hours, minutes, and seconds.

Write a Python program that:
- Accepts the total event duration in seconds as input.
- Calculates how many hours, minutes, and seconds it corresponds to.
- Displays the output in the format:
  Hours: x, Minutes: y, Seconds: z

Sample Input:
Total event duration in seconds: 3672

Sample Output:
Hours: 1, Minutes: 1, Seconds: 12'''









total_seconds=int(input("Total event duration in seconds:"))
hours=total_seconds//3600
rem_min=total_seconds%3600
minutes=rem_min//60
seconds=rem_min%60
print(f"Hours:{hours},Minutes:{minutes},Second:{seconds}")

