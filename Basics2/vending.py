'''You insert an amount into a vending machine. It returns coins using the largest denominations possible (₹10 and ₹5).

Write a Python program that:
- Accepts the total amount.
- Calculates how many ₹10 coins and ₹5 coins will be dispensed.
- Displays the result.

Example:
Amount = ₹35
Output = ₹10 x 3, ₹5 x 1'''






total_amount=int(input("Amount="))
ten_coins=total_amount//10
rem_coins=total_amount %10
five_coins=rem_coins//5
print(f" Amount = rs{total_amount}\n Output= rs10 x {ten_coins} , rs5 x {five_coins}")

