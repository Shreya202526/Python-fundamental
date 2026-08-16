s1=input("Enter the String1")
s2=input("Enter the String2")
equal=0
for i in range(len(s1)):
    if len(s1)==len(s2):
        if sorted(s1)==sorted(s2):
            equal=1
        else:
            equal=0
if equal==1:
    print("Equal String")
else:
    print("Not Equal String")   


