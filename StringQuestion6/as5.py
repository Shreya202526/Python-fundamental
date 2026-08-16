''' 5. Social Media Hashtag Trend Window

A social media company wants to analyze the smallest substring containing all unique characters from a hashtag.

### Input:

text
aabcbcdbca


### Output:

text
dbca


### Explanation:

dbca contains all unique characters: a,b,c,d

---'''
s=input("Enter the String")
new_string=""
smallest=""
for x in s:
    if x  not in new_string:
        new_string+=x
print(new_string)
ans=""
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        sub=s[i:j]
        flag=True
        for ch in new_string:
            if ch not in sub:
                flag=0
                break
        if flag==1:
            if ans=="" or len(sub)<len(smallest):
                smallest=sub
                ans=sub
print("Smallest String:",ans)


