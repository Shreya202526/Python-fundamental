'''9. Neon Number LED Unlock Game
You're programming a new LED display game. The game level unlocks only when a neon number is entered.

A neon number is a number where the sum of the digits of its square is equal to the number itself.
Example: 9 → 9² = 81 → 8 + 1 = 9

Accept a number from the player.
Check whether it is a neon number using loops.

If true, display:
Glowing Success! You've found the Neon Number!

Otherwise display:
Try again! Not quite glowing yet.

Input:
9'''


n=int(input("Enter the number:"))
square=n**2
sum=0
while square>0:
      d=square%10
      sum=sum+d
      square=square//10
if sum==n:
      print("Glowing Success! You've found the Neon Number!")
else:
      print("Try again! Not quite glowing yet.")


n=int(input("Enter the number:"))
square=n**2
sum=0
for i in range(0,len(str(square))):
      d=square%10
      sum=sum+d
      square=square//10
      print(sum)
if sum==n:
      print("Glowing Success! You've found the Neon Number!")
else:
      print("Try again! Not quite glowing yet.")
