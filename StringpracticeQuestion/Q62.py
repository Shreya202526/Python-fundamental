'''62 Count vowels and consonants. S = "apple" Vowels: 2, Consonants: 3'''
s=input("Enter the string=")
vol=0
const=0
for i in range(len(s)):
    ch=s[i]
    if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
        vol+=1
    else:
        const+=1
print(f"Vowels: {vol}, Consonants: {const}")
