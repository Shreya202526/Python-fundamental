'''2. University Admission System

A university decides admission based on marks, entrance score, and category of the student.

If marks are 70 or above, then check entrance score. If entrance score is 80 or above, then check category. If general, admit; otherwise admit with scholarship. If entrance score is less than 80, then check if marks are 85 or above. If yes, admit under management quota; otherwise reject. If marks are below 70, then check if category is not general and marks are at least 60. If yes, check entrance score. If it is 70 or above, waitlist; otherwise reject. If none of these conditions match, reject.

Input:
Marks = 72
Entrance Score = 85
Category = general

Output:
Admission Status = Admitted'''



marks =int(input("Marks="))
score=int(input("Entrance score="))
category=input("Category=")
if marks>=70:
   if score>=80:
          if category.lower()=="general":
             print("Admission status=admitted")
          else:
             print("Admission status=admit with scholarship")
   elif score<=80:
        if marks>=85:
             print("Admission status=admit under management quota")
        else:
             print("Admission status=reject")

   elif score<=70:
        if category.lower()==" Admission status=not general":
            if score>=70:
             print("Admission status=wait list")
        else:
             print("Admission status=reject")
else:
   print("Admission status=reject")


      

