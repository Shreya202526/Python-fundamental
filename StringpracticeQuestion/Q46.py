'''46 Check if a substring appears at both the start and end. S = "abcabca", Sub = "abca" TRUE'''


s=input("Enter the String=")
sub=input("Enter the Substring=")

first = s[:len(sub)]
last = s[-len(sub):len(s)]

if first == sub and last == sub :
    print(True)
else :
    print(False)    
