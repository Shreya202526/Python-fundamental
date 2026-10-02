'''Reverse each word. S = "cat dog" "tac god"

s=input("Enter the string:")
new_string=s.split()
result=""
for x in new_string:
    result+=x[::-1]+" "
print(result)'''


s=input("enter the string:")
n=s.split()
result=""
for i in n:
    result+=i[::-1]+" "
print(result)