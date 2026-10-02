'''2.
Find the Most Frequently Occurring Word
News Channel Keyword Analyzer

A news agency analyzes breaking news headlines to identify the most repeated keyword in a report.

Write a Python program to find the word with the highest frequency.

Input:
india won the match and india created history
Output:
india'''

'''s=input("Enter input:")
new_string=s.split()
c=0
for i in new_string:
    count=0
    print(i)
    for j in new_string:
        count+=1
    if count>c:
        c=count
        max=i
print(max)
print(c)
'''


s=input("Enter message :")
w=s.split()
vis=""
max=""
c=0
for ch in w:
    if ch not in vis:
        vis =vis+ch+" "
        count=s.count(ch)
        if count>c:
            c=count
            max=ch
print(max)