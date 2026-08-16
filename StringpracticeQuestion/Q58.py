'''58 Rotate characters by 2 positions to the left. S = "abcde" "cdeab"'''
s=input("Enter the string")
str2=s[0:2]
new=s[len(str2):len(s)]+str2
print(new)
print(str2)
