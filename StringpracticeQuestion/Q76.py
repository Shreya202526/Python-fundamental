
'''76 Find the longest common suffix among strings. Strings = ["baking", "making", "taking"] "king"

new_string=input("enter the string=").split()
least=0
least_word=""
for x in new_string:
    if len(x)>least:
        least_word=x
        least=len(x)
        i=0
        while i<len(least_word):
            word=least_word[i:len(least_word)]
            print(word)
            count=0
            for x in new_string:
                if x.endswith(word):
                    count+=1
            if count==len(new_string):
                print(word)
                break
            i=i+1
print(least)
'''


n=input("Enter string ").split()
s=n[0]
i=1
res=""
temp=""
temp1=""
while i<len(n):
    c=n[i]
    j=0
    while j<len(s) and j<len(c):
        if i==1:
             if s[j]==c[j]:        
                temp1+=s[j]
         
             else:
                 break
        else:
            k=0
            temp1=""
            while k<len(temp) and k<len(c):
                 if temp[k]==c[k]:              
                     temp1+=temp[k]
                 
                      
                 else:
                     break
            
                 k+=1
        temp=temp1

        j+=1  
    i+=1


print(temp)