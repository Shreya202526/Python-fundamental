'''57 Merge two strings alternatively (char by char). S1 = "ABC", S2 = "def" "AdBeCf"'''

s1=input("Enter the string1=")
s2=input("Enter the string2=")
result=""
for i in range(len(s1)):
        result+=s1[i]+s2[i]
print(result)