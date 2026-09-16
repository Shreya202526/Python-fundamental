def Perfect(n):
      sum=0
      i=1
      while i<=n//2:
           if n%i==0:
                sum+=i
           i+=1
      if sum==n:
           print(f"{n} is  perfect number")
      else:
           print(f"{n} is Not perfect number")
def pallindrome(n):
     original=n
     i=n
     rev=0
     while i>0:
          d=i%10
          rev=rev*10+d
          i=i//10
     if rev==n:
          print(rev)
          print(n)
          print("pallindrome ")
     else:
          print(rev)
          print(n)
          print("Not pallindrome")
def reverse(n):
     rev=0
     i=n   
     while i>0:
        d=i%10
        rev=rev*10+d
        i=i//10
     return rev
def strong(n):
     result=0
     i=n
     while i>0:
         d=i%10
         print("digit",d)
         fact=1
         for j in range(1,d+1):
            fact*=j  
            print("fact",fact)
         result+=fact
         print("Result",result)
         i=i//10
     if result==n:
          print(f"{n} is Strong Number")
     else:
          print(f"{n} is not Strong number")
def armstrong(n):
          p=len(str(n))
          sum=0
          i=n
          while i>0:
               d=i%10
               pwd=d**p
               sum+=pwd
               i=i//10
          if n==sum:
           print(f"{n} is Armstrong Number")
          else:
            print(f"{n} is not Armstrong Number")
def prime(n):
    if n<2:
             return "Not prime"
    else:
     for i in range(2,n//2):
        if n%i!=0:
            return "Prime"
        else:
            return "Not Prime"     
def evenodd(n):
     if n%2==0:
          return "Even "
     else:
          return "Odd"
def factorial(n):
     fact=1
     for i in range(1,n+1):
          fact*=i
     return fact
def sumdigit(n):
     sum=0
     i=n
     while i>0:
          d=i%10
          sum+=d
          i=i//10
     return sum
def numberofdigit(n):
    return len(str(n))
def automorphic(n):





while True:
    print("========================================")
    print("   NUMBER ANALYSIS SYSTEM       ")
    print("=======================================")
    print("1. Check Perfect Number")
    print("2. Check Palindrome Number")
    print("3. Check Strong Number")
    print("4. Check Armstrong Number")
    print("5. Check Prime Number")
    print("6. Check Even or Odd")
    print("7. Find Factorial")
    print("8. Find Sum of Digits")
    print("9. Reverse a Number")
    print("10. Find Number of Digits")
    print("11. Check Automorphic Number")
    print("12. Check Neon Number")
    print("13. Check Spy Number")
    print("14. Check Harshad Number")
    print("15. Exit")
    choice=int(input("Enter your choice: "))
    match choice:
        case 1:
            n=int(input("Enter the number:"))
            Perfect(n)
        case 2:
            n=int(input("Enter the number: "))
            pallindrome(n)
        case 3:
              n=int(input("Enter the number: "))
              print(strong(n))
        case 4:
              n=int(input("Enter the number: "))
              armstrong(n)
        case 5:
              n=int(input("Enter the number: "))
              prime(n)
        case 6:
              n=int(input("Enter the number: "))
              print(evenodd(n))
        case 7:
              n=int(input("Enter the number: "))
              print(factorial(n))
        case 8:
              n=int(input("Enter the number: "))
              print(sumdigit(n))
        case 9:
            n=int(input("Enter the number: "))
            print(reverse(n))
        case 10:
             n=int(input("Enter the number: "))
             print(numberofdigit(n)) 
        case 11:
              n=int(input())