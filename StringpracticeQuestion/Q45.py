'''45Check whether a string starts with or ends with another string. S = "apple pie", 
Prefix = "apple",
 Suffix = "pie" Start: True, End: True'''
s=input("Enter the string=")
prefix=input("Enter prefix=")
suffix=input("Enter suffix=")
new_string=s.split()
if new_string[0]==prefix:
     start=True
else:
     end=False
if new_string[0]!=suffix:
     end=True
else:
     start=False
print("Start:",start,"End:",end)
     

