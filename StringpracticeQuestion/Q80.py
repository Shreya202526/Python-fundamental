'''80 Print list items containing all characters of a given word. List = ["apple", "plea"],
 Word = "pal" "apple", "plea"'''


List=["apple","plea"]
word=input("Enter the word")
for x in List:
    for y in word:
     if y not in x:
        break
    else:
       print(x)
        


         

      

   
         
          