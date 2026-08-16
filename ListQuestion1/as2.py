'''2.Employee Salary Processing
Store employee salaries in a List and calculate details.

Requirements:

Store salaries
Find average salary
Display salaries greater than average
Remove salaries below 15000

Test Cases:

Input: [10000, 20000, 30000] → Average = 20000, Above Average = 30000
Input: [15000, 15000, 15000] → Average = 15000
Input: [5000, 7000] → Remaining List = []'''

n=int(input("Enter the size of list"))
nums=[]
sum=0
avg=0
above_avg=0
rem_salary=15000
remaining=[]
for i in range(n):
    x=int(input("Enter Element="))
    nums.append(x)
print(nums,end="->")
for x in nums:
     sum+=x
     avg=sum/n
     above_avg=avg
     if x>=above_avg:
       above_avg=x
     elif x>rem_salary:
        remaining.append(x)
        
print("Average:",avg,end=",")
print("Above Avg",above_avg,end=",")
print("Remaining List:",remaining)