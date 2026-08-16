'''1.
=========================================
STUDENT CLUB MEMBERSHIP SYSTEM
=========================================

A college has two clubs:
1. Coding Club
2. Robotics Club

Store student IDs of both clubs using sets.

Menu:
1. Add Student to Coding Club
2. Add Student to Robotics Club
3. Display Students in Coding Club
4. Display Students in Robotics Club
5. Find Students in Both Clubs
6. Find Students Only in Coding Club
7. Find Students Only in Robotics Club
8. Display All Unique Club Members
9. Display Total Unique Club Members
10. Exit

Requirements:
- Use two sets.
- Apply intersection, difference, and union operations.'''

coding_club=set()
robotics_club=set()
while True:
   
  print("Menu:")
  print("1. Add Student to Coding Club")
  print("2. Add Student to Robotics Club")
  print("3. Display Students in Coding Club")
  print("4. Display Students in Robotics Club")
  print("5. Find Students in Both Clubs")
  print("6. Find Students Only in Coding Club")
  print("7. Find Students Only in Robotics Club")
  print("8. Display All Unique Club Members")
  print("9. Display Total Unique Club Members")
  print("10. Exit")

  choice=int(input("Enter your choice="))


  match choice:
    case 1:
         n=int(input("Enter the number of students you want to add:"))
         for i in range(1,n+1):
          student=input(f"Enter the name of the student {i}: ")
          coding_club.add(student)
         print("Students Added to the Coding clud")

    case 2:
         n=int(input("Enter the number of students you want to add:"))
         for i in range(1,n+1):
          student=input(f"Enter the name of the student {i}: ")
          robotics_club.add(student)
         print("Students Added to the robotics clud")

    case 3:
      if coding_club:
       print(coding_club)
      else:
       print("No Student in coding club")

    case 4:
         if coding_club:
          print(robotics_club)
         else:
          print("No Student in robotics club")

    case 5:
         if coding_club and robotics_club :
            both=coding_club.intersection(robotics_club)
            print(both)
         else:
            print("Firstly add student in both club")   


    case 6:
        if coding_club:
          only_coding=coding_club.difference(robotics_club)
          print(only_coding)
        else:
          print("No Member in Coding club")

    case 7:
        if robotics_club:
          only_robotics=robotics_club.difference(coding_club)
          print(only_robotics)
        else:
          print("No Member in Robotics club")


    case 8:
        if coding_club and robotics_club:
          All_unique=coding_club.union(robotics_club)
          print(All_unique)
        else:
          print("firstly add member in both club")
    case 9:
        if coding_club and robotics_club:
          total_memebers=len(coding_club.union(robotics_club))
          print(total_memebers)
        else:
          print("firstly add member in both club")
    case 10:
        print("Exitingggg......")
    case __ :
        print("you enter invalid choice")
   
        
        

          
       
                