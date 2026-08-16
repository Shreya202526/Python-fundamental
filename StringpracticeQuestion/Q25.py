'''25Count total words in a string. S = "This is a test"  4''' 
s=input("Enter the string")
count=0
for i in range(len(s)):
    if i==0 or s[i-1]==" ":
        count+=1
print(count)