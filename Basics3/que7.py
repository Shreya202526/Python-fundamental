'''In cricket, overs are given in decimal format (e.g., 48.3 means 48 overs and 3 balls). Convert overs into total balls and calculate run rate.

Input:
Total runs = 275
Overs = 48.3

Expected Output:
Total Balls = 291
Run Rate = 5.67'''

total_run=int(input("Total runs="))
ovr,balls=map(int,input("Overs=").split("."))
total_balls=ovr*6+balls
actual_ovr=ovr+balls/60
run_rate=total_run/actual_ovr
print(f"Total Balls={total_balls}\n Run Rate={run_rate}") 












