'''59 Rotate characters by 3 positions to the right. S = "abcde" "cdeab"'''
s=input("Enter the string")
str2=s[-3:len(s)]
new=str2+s[0:len(s)-3]
print(new)
print(str2)
