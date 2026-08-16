'''70 Compare the number of times 'the' and 'is' appear. S = "the cat is on the mat" the: 2, is: 1 (theis)'''
s=input("enter the string")
a=input("enter the word:")
b=input("enter the word:")
a2=0
b2=0
new_string=s.split()
for i in range(len(new_string)):
    if new_string[i]==a :
        a2+=1
    elif new_string[i]==b:
        b2+=1
    else:
        pass
print(f"the: {a2}, is: {b2} ")
    