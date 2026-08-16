'''3.
Reverse Sentence + Reverse Each Word(3 marks)

Secret Military Communication Decoder
A defense organization stores highly confidential messages in encrypted form.
To decode the message:

1. Reverse the entire sentence.
2. Reverse every individual word.
3. Store the final result back into the original string variable.

You must use the split() method.
Input:


Python is powerful


Output:


lufrewop si nohtyP'''


s=input("Input:")
new_string=s.split()
new_word=""
for x in new_string:
       word=new_string[::-1]
for y in word:
    new_word=new_word+y[::-1]+" "
print(word)
print(new_word)


    


