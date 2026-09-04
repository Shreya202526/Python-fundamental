'''75 Find the longest common prefix among strings. Strings = ["flower", "flow", "flight"] "fl"'''

new_string=input("enter the string=").split()
least=len(new_string[0])
least_word=new_string[0]
for x in new_string:
    if len(x)<least:
        least_word=x
        least=len(x)

i=0
while i<len(least_word):
    word=least_word[:len(least_word)-i]#main code
    count=0
    for x in new_string:
        if x.startswith(word):
         count+=1
    if count==len(new_string):
         print(word)
         break
    i=i+1


