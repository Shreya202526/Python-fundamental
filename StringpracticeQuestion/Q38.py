'''38 Reverse words without using split(). S = "a b c" "c b a"'''

s=input("Enter the string")
result=""
for i in range(len(s)-1,-1,-1):
    result=result+s[i]
    
print(result)
