'''1. Smart Log File Error Pattern Detector

A cybersecurity company stores server logs containing repeated system activity characters.

To detect suspicious looping behavior, the analytics team wants a Python program that finds the longest repeating substring present in the log file.

If multiple substrings have the same length, print the first one found.

 Input:

text
abcabcbb


Output:

text
abc'''


s=input("Input")
long=""
for i in range(len(s)):
    temp=""
    for j in range(i,len(s)):
            temp+=s[j]
            c=0
            for k in range(len(s)-len(temp)+1):
             if s[k:k+len(temp)]==temp:
                 c+=1
            if c >= 2 and len(temp) > len(long):
               long = temp  
print("Longest String",long)
