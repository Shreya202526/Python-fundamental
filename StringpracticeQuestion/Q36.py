'''Reverse order of words. S = "one two three" "three two one"'''


s=input("Enter the string:")
new_string=s.split()
print(" ".join(new_string[::-1]))