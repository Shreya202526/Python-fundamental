'''2. Reverse Sentence + Reverse Each Word

Secret Military Communication Decoder
A defense organization stores highly confidential messages in encrypted form.
To decode the message:

1. Reverse the entire sentence.
2. Reverse every individual word.
3. Store the final result back into the original string variable.

You must use the split() method.
Input:





Output:


lufrewop si nohtyP'''

s=input("Enter the String:")
new_string=s.split()
result=""
i=0
while i<len(new_string):
        str2=new_string[::-1]
        word=str2[i]
        new_word=""
        
        j=len(word)-1
        while j>=0:
              new_word=new_word+word[j]
              j=j-1
        result=result+new_word+" "
        i=i+1

print(str2)
print(new_word)
print(result)