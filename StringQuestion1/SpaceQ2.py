'''2.
Space Counter in Chat Messages
A chat application wants to calculate how many spaces are used in a message.
Input: Enter chat message: Good morning everyone how are you
Output: Total spaces: 5'''

s=input("Enter the string=")
space=0
i=0
while i<len(s):
      if s[i-1]==" ":
         space=space+1
      i=i+1
print("Total space=",space)

