'''4. Program should work for both uppercase and lowercase letters.
 Find the Shortest Word in a Sentence
Telecom SMS Cost Optimization System
A telecom company charges customers based on the length of words used in bulk SMS campaigns.
The company wants to identify the shortest word in every message for analytics purposes.
Write a Python program to find the shortest word from a given sentence.
Input:

Python is very easy to learn


Output:


is'''

s=input("Enter the String:")
new_string=s.split()
length=""
i=0
while i<len(new_string):
      shortest=new_string[1]
      current_word=new_string[i]
      if len(shortest)<=len(current_word):
         current_word==shortest
      i=i+1
print(shortest)
      

