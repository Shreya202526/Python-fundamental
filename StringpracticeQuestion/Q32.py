'''32Count frequency of each word. S = "apple banana apple" apple: 2, banana: 1'''
s=input("Enter the string")
new_string=s.split()
done=""
for i in new_string:
    c=0
    for j in new_string:
        if i==j :
            c+=1
    if i not in done:
        print(f"{i}:{c}")
        done+=i
            

    


