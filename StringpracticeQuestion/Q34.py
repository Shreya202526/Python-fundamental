'''4 Find the shortest word. S = "find the shortest word" "the"'''
s=input("Enter the string ")
new_string=s.split()
smallest=s
for x in new_string:
    if len(x)<len(smallest):
        smallest=x
print(smallest)