'''13 Get the Unicode code point before index. S = "Hello", Index = 1 72 (Unicode for 'H')'''

s=input("Enter the String:")
index=int(input("Index:"))
print(ord(s[index-1]))