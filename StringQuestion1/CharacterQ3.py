'''Character Occurrence Checker in Product Review
An e-commerce website wants to know how many times a particular character appears in a product review.
Input: Enter product review: this product is really good Enter character to check: o
Output: Character 'o' occurs: 4 times'''

s=input("Enter the String =")
ch=input("Enter character to check=")
times=0
i=0
while i<len(s):
      if s[i]==ch:
         times+=1
      i+=1
print("Character",chr,"occurs",times) 
