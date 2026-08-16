'''33 Find the longest word. S = "find the longest word" "longest"'''

s=input("Enter the string ")
new_string=s.split()
longest=""
for x in new_string:
    if len(x)>len(longest):
        longest=x
print(longest)
