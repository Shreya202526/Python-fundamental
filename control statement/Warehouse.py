'''8. A warehouse management system needs to identify the highest stock level among six different storage units to prioritize dispatch.
 The system should take the quantity of items stored in six units as input. It should compare all six values using nested conditions
 and determine which unit has the maximum stock. Display the highest stock value among all six units.

Input:
Unit1 = 120
Unit2 = 450
Unit3 = 300
Unit4 = 275
Unit5 = 500
Unit6 = 390

Output:
Highest Stock = 500'''
a=int(input("Unit1="))
b=int(input("Unit2="))
c=int(input("Unit3="))
d=int(input("Unit4="))
e=int(input("Unit5="))
f=int(input("Unit6="))
if a>=b:
   if a>=c: 
       if a>=d: 
           if a>=e:
                   if a>=f:
                       print("a is greater")
                   else:
                       print("f is greater")
           else:  
                if e>=f: 
                    print("e is greater")
                else:
                    print("f if greater")
       else:
               if d>=e:
                     if d>=f:
                           print("D id greater")
                     else:
                           print("f is greater")
               else:
                    if e>=f:
                       print("e is greater")
                    else:  
                       print("f is grater")   

   else: 
        if c>=d:
              if c>=e:
                 if c>=f:
                        print("cis greater")

                 else:
                      print("f is greater")
              else:
                   if  e>=f:
                       print("E is greater")

                   else:
                       print("F is greatrer")
        else:
             if d>=e:
                 if d>=f:
                    print("d is grater")
                 else:
                    print("f is greater")
             else:
                  if e>=f:
                    print("e is graeter")
                  else :
                    print(" f is graeter")
else:
     if b>=c: 
         if b>=d: 
             if b>=e:
                   if b>=f:
                       print("b is greater")
                   else:
                       print("f is greater")
             else:  
                 if e>=f: 
                    print("e is greater")
                 else:
                    print("f if greater")
     else:
               if d>=e: 
                  if d>=f:
                       print("d is greater")
                  else:
                       print("f is greater")
               else:  
                 if e>=f: 
                    print("e is greater")
                 else:
                    print("f if greater")
    
        













                     




                      
  

        else:     
else:

      