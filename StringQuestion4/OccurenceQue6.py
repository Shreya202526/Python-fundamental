'''6. Find Occurrence of a Word in a String
Product Review Analysis System
An e-commerce company wants to analyze customer reviews.
The company wants a Python program to count how many times a particular word appears in a review.
Input Sentence:
iphone is good and iphone battery is strong
Word:
iphone
Output:
2
'''


s=input("Enter the String=")
word=input("Word=")
new_string=s.split()
count=0
i=0
while i<len(new_string):
      ch=new_string[i]
      if ch==word:
            count=count+1
      i=i+1
print(count)



