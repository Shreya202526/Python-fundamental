'''79 Divide a string into n equal parts. S = "abcdef", n = 3 "ab", "cd", "ef"'''

s=input("Enter the String=")
n=int(input("Enter size of equal parts="))
parts=int(len(s)/n)
for i in range(0,len(s),parts):
    print(s[i:i+parts],end=" ")
