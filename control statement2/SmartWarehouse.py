'''5. Smart Warehouse Dispatch System

A warehouse decides dispatch strategy based on stock availability, priority level, and delivery distance.

If stock is at least 100, then check priority. If high priority, then check distance. If distance is up to 200, dispatch immediately; otherwise use fast courier. If priority is not high, then check if stock is at least 300. If yes, bulk dispatch; otherwise normal dispatch. If stock is less than 100, then check if stock is at least 50. If yes, and priority is high, partially dispatch; otherwise hold. If stock is below 50, mark out of stock.

Input:
Stock = 120
Priority = high
Distance = 300

Output:
Dispatch Status = Dispatch via Fast Courier'''


stock=int(input("Stock="))
priority=input("Priority=")
dist=int(input("Distance="))
if stock>=100:
        if priority.lower()=="high":
           if dist<=200:
              print("Dispatch immediately")
           else:
                print("fast courier ")  
        else:
              if stock>=300: 
                 print(" bulk Dispatch ")
              else:
                 print(" Normal Dispatch")  
else: 
        if stock>=50:
            if priority.lower()=="high":
                print("Dispatch partially")
            else:
                 print("hold")
        else:
              print("out of stock")      




