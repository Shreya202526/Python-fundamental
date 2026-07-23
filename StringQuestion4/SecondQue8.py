'''8.
Find the Second Highest Repeating Character in a String
Social Media Trend Analysis System
A social media company analyzes hashtags and user comments to identify trending character patterns.
The analytics team wants a Python program to find the character with the second highest frequency in a given string.
This helps detect secondary trending patterns in user activity.

Input:

aaabbbbccddeee

Output:

e


Explanation:

b occurs 4 times → highest
e occurs 3 times → second highest

Condition:

Program should work for both uppercase and lowercase letters.
Spaces should be ignored.'''


# s=input("Input:")
# c=0
# max=""
# n=""

# for i in s:
#     count=0
#     for j in s:
#         if i==j:
#             count+=1

#     if count>c:
#         c=count
        
#         max=i
        
#         n+=str(c)+max
#         # print(s)

# # print(max)
# # print(c)

# for i in  range(len(n)):
#     if i<c:
#         print(f"{n[i+1]} -> {n[i]}")
#         break


# Input:

# aaabbbbccddeee

# Output:

# e

s=input("Enter : ")

largest=0
l_ans=""
for i in s:
    count=0
    for j in s:
        if i==j:
            count+=1
    if largest<count :
        largest=count
        l_ans=i

    # if second<largest:
    #     second=count
    #     ans=i

print(l_ans)

s_ans=''
second=0


for i in s:
    count=0
    for j in s:
        if i==j:
            count+=1
    if largest!=count and  count >= second:
        second=count
        s_ans=i
        
print(s_ans)