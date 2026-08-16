"""54 Replace all duplicate characters with '$'. S = "hello" "he$lo"
"""
s=input("Enter the String=")
result=""
vis=""
for i in range(len(s)):
    ch=s[i]
    if ch not in vis:
        vis+=ch
        if s.count(ch)>1:
            result+="$"
        else:
            result+=ch
    else:
        result+=ch
print(result)
