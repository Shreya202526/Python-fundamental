'''4.  Instant Messaging Word Encryption System

A messaging application wants to temporarily encrypt messages during
transmission. The encryption rule is to reverse every word individually
while keeping the word positions unchanged.

Input: Enter message: java is powerful

Output: Encrypted Message: avaj si lufrewop'''

s=input("Enter message=")
new_str=""
new=""
i=0
while i<len(s):
      new_str=s.split()
      i=i+1
print(new_str)
j=0
while j<len(new_str):
      ch=new_str[j]
      new=new+ch[::-1]+" "
      j=j+1
print("Encrypted Message:",new, end=" ")
