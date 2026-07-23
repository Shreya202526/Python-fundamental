'''6.
 Advanced Student Registration Data Processing System

A national university is developing an intelligent registration portal.Students enter registration codes using uppercase letters, lowercaseletters, digits, and special symbols. Due toinconsistent data entry,the administration wants the system to standardize and process theinformation before storing it.Conditions: - Ignore all special characters (@ # $ % & * - _) - Separate alphabets and digits - Convert all alphabets to lowercase - Removeduplicate alphabets - Arrange alphabets in ascending order - Arrange digits in descending order - Display alphabets first and digits later -
If no digits are found, display “No Digits Found”'''

s=input("Enter registration code:")
letter=""
digit=""
i=0
while i<len(s):
      ch=s[i]
      if ch>='a' and ch<='z' or ch>='A' and ch<='Z':
         letter=letter+(ch.lower())
      elif ch>='0' and ch<='9':
         digit=digit+ch
      i=i+1
      k=0
      uniq=""
      while k<len(letter):
            new_ch=letter[k]
            if new_ch not in uniq:
               uniq=uniq+new_ch
            k=k+1
print(digit)
print(letter)
print(uniq+digit)