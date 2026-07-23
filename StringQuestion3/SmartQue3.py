'''3.  Smart Chat Message Cleaner

A social media company noticed that users often enter messages with
unnecessary spaces. To improve readability and storage efficiency, the
system should remove extra spaces and keep only a single space between
words.

Input: Enter message: Java is easy

Output: Cleaned Message: Java is easy'''

s=input("Enter Message:")
result=""
i=0
while i<len(s):
      if i==0 or s[i]!=" ":
         result=result+s[i]
      else:
        if result == "" or result[-1] != " ":
            result = result + " "
      i=i+1
print(result)