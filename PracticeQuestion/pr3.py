'''A cricket academy wants to analyze player performance. Each player's information is stored as a tuple.

Tuple Format:

(player_id, player_name, runs_scored)

Requirements:

Read N player records from the user and store them as tuples in a list.
Display all player records.
Find and display the player who scored the highest runs.
Find and display the player who scored the lowest runs.
Calculate and display the total runs scored by all players.
Calculate and display the average runs scored.
Display players who scored more than 50 runs.

Test Case:

Input:

Enter number of players: 5

101 Virat 82
102 Rohit 45
103 Gill 120
104 Hardik 38
105 SKY 76

Expected Output:

All Players:
(101, 'Virat', 82)
(102, 'Rohit', 45)
(103, 'Gill', 120)
(104, 'Hardik', 38)
(105, 'SKY', 76)

Highest Scorer:
(103, 'Gill', 120)

Lowest Scorer:
(104, 'Hardik', 38)

Total Runs:
361

Average Runs:
72.2

Players Scoring More Than 50 Runs:
(101, 'Virat', 82)
(103, 'Gill', 120)
(105, 'SKY', 76)
'''

n=int(input("Enter the number of player"))
list=[]
player=()
for i in range(n):
    player_id =int(input("Enter the id of player:"))
    player_name=input("Enter the name of the player: ")
    runs_scored=int(input("Enter the score of the player: "))
    player=(player_id, player_name, runs_scored)
    list.append(player)
print(list)
for x in list:
    print(x)


high_score=list[0][2]
high_name=""
low_score=list[0][2]
low_name=""
total=0
print("All PlAYER")
for i in list:
    print(i)
    total+=i[2]
    if i[2]>high_score:
        high_score=i[2]
        high_name=i

    if i[2]<low_score:
        low_score=i[2]
        low_name=i
print()
print("Highest Scorer:")   
print(high_name)

print()
print("Lowest Scorer:")
print(low_name)

print("Total Score")
print(total)


print("Player score 50 more")
for i in list:
 if i[2]>50:
    print(i)
