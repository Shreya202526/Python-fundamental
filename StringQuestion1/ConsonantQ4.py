'''4.
Consonant Counter in Student Name Record
A school management system wants to count how many consonants are present in student names.
Input: Enter student name: Ajay Singh Thakur
Output: Total consonants: 11

NOTE:

Ignore case sensitivity (treat A and a same)
Consider only English alphabets for vowel/consonant counting
Vowels: A, E, I, O, U
'''
s=input("Enter the String").lower()
consonant=0
i=0
while i<len(s):
    if s[i]>='a' and s[i]<='z':
      if s[i]!='a' and s[i]!='e' and s[i]!='i' and  s[i]!='o' and s[i]!='u':
           consonant=consonant+1
    i=i+1
print(consonant)
