'''4. Prime Security Code Checker – Advanced

A high-security lab accepts only prime numbered access codes.

When a user enters a number, the software must:

- Check whether number is prime
- If prime, print next immediate prime number
- If not prime, print previous immediate prime number

Write a program using loops only.

Input:
29

Output:
Prime Number
Next Prime = 31'''


'''n=int(input("Enter the number"))
num=n
for i in range(2,n//2):
      if n%i==0:
         num=num-1
         print(num)
         break
         for i in range(2,num2//2):
             num2=num-1
             if num2%i==0:
                num2=num2-1
                print(num2)
                break
         else:
                print("previous prime:",num2)'''


n=int(input("enter the number="))
num=n
x=-1
for i in range(2,n//2):
   if n%i==0:
      print(" not prime")
      break
else:
    print("prime no.",n)
    x=1
    num=n+1     
while True:
       print("num prime: ",num)
       for i in range(2,num//2+1):
        if num%i==0:

           num=num+x
           break
       else:
            next=num
            print("Next prime ID",next)
            break
print("num prime: ",num)