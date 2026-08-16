'''QNo 8:--
SMART TEXT PROCESSING SYSTEM

A software company is developing a Smart Text Processing System for
handling user messages. Different users require different text
transformations. To avoid creating separate applications, the company
wants a menu-driven program where users can select operations according
to their requirements.

The system should continue executing until the user selects Exit.

====================================================== MENU
======================================================

===== Smart Text Processing System =====

1.  Reverse Complete String
2.  Reverse Every Word
3.  Reverse Word Order
4.  Exit

====================================================== Choice 1 :

Conditions: - Reverse the complete string - Ignore extra spaces - Keep
special characters (@,#,$,%) in their original positions - Do not use
built-in reverse functions

Example: Input: ja@va#py

Output: yp@av#aj

Test Case 1: ab@cd#ef Output: fe@dc#ba

Test Case 2: py@th#on Output: no@ht#yp

Test Case 3: java@proOutput : orpa@vaj

====================================================== Choice 2 :

Conditions: - Reverse every word separately - Words containing digits
should not be reversed - Ignore extra spaces between words - First
letter of each reversed word should become uppercase

Example: Input: java is easy123 programming

Output: Avaj Si easy123 Gnimmargorp

Test Case 1: python full stack22 developer Output: Nohtyp Lluf stack22
Repoleved

Test Case 2: hello java99 world Output: Olleh java99 Dlrow

====================================================== Choice 3 :

Conditions: - Reverse order of words - Remove duplicate words - Ignore
case while checking duplicates - Keep only first occurrence

Example: Input: Java python Java react Python

Output: React Python Java

Test Case 1: HTML CSS HTML Java CSS Output: Java CSS HTML

Test Case 2: Python React Java Python React Output: Java React Python

====================================================== Choice 4
======================================================

Program Closed Successfully'''

while True: 
   print("===== Smart Text Processing System =====")
   print("1.  Reverse Complete String")
   print("2.  Reverse Every Word")
   print("3.  Reverse Word Order")
   print("4.  Exit")
   choice=int(input("Enter your choice"))
   match choice:
         case 1:
              s=input("Enter the String:")
              s1=""
              s2=""
              for i in range(len(s)-1,-1,-1):
                   ch=s[i]
                   if ch.isalpha():
                    s1=s1+ch
                   else:
                    s2=ch+s2
              i=0
              j=0
              s3=""
              for k in s:
                if not(k.isalpha()):
                   s3+=s2[i]
                   i+=1
                else:
                    s3+=s1[j]
                    j+=1
              print(s3)
              print(s1)
              print(s2)
         case 2:
              s=input("Enter the string")
              new_string=s.split()
              temp=""
              for i in range(len(new_string)-1):
                   if new_string[i] not in temp:
                      temp=temp+new_string[i]+" "
              print(temp)
              temp=temp.split()
              print(" ".join(temp[::-1]))
         case 3:
           s=input("Enter the string")
           new_string=s.split()
           str2=""
           result=""
          
           for x in new_string:
              found=False
              for i in x:
               if i.isnumeric():
                 found=True
                 break
              if found:
               str2=str2+x+" "
              else:
               str2=str2+x[::-1]+" "
           for i in range(len(str2)):
              if i==0 or str2[i-1]==" ":
                 if str2[i].lower():
                   result=result+str2[i].upper()
                 else:
                    result=result+str2[i]
              else:
                 result=result+str2[i]
                              
           print(result)
          
             
 







 