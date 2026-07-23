
while True:
     print("1.Add two number")
     print("2.Even or Odd")
     print("3.Square root")
     print("4.Exit")
     choice=int(input("Enter the choice:"))
     match choice:
           case 1:
                a=int(input("Enter First Number"))
                b=int(input("Enter Second Number"))
                print("result",a+b)
           case 2:
                n=int(input("Enter the number"))
                if n%2==0:
                       print("Even")
                else:
                       print("odd")
           case 3:
                n2=int(input("Enter the number"))
                print("Result=",n2*n2)            
           case 4:
                print("Exit------")
                break
     again=input("Do You want to continue........")      
     match again: 
           case "yes":
                 continue
           case "no":
                 break
           case __ :
                print("kuch bhiiiii") 
                break 
print("Done")       

    