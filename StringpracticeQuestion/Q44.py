'''44Check if two strings are anagrams. S1 = "listen", S2 = "silent" TRUE'''

s1=input("Enter the string1:")
s2=input("Enter the string2:")
if len(s1)==len(s2):
    if sorted(s1)==sorted(s2):
        print("Anagram")
    else:
        print("Not anagram")
else:
    print("Not Anagram")
    
        