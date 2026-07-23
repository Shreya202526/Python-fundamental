'''1.Vowel Counter in Customer Feedback
 A company wants to analyze customer feedback messages by counting how many vowels are present in the feedback.
Input: Enter feedback message: Hello Customer Service
Output: Total vowels: 8'''



s=input("Enter the String").lower()
vowel=0
i=0
while i<len(s):
      if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u':
         vowel=vowel+1
      i=i+1
print(vowel)
