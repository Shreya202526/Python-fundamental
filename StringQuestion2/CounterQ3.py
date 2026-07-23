'''Word Counter in Complaint Message

A customer care system wants to count how many words are present in a complaint message.

Input:
Enter complaint: Delivery was delayed again today

Output:
Total words: 5'''


s=input("Enter complaint")
print(s)
length=s.split()
print("Total words:",len(length))
