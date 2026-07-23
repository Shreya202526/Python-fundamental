'''QNO 7:
 Advanced Smart Chat Compression Expansion System

A messaging application stores repeated characters in compressed form to
reduce storage space. Before displaying messages to users, the system
should reconstruct the original message.

The application team has introduced additional rules.

Conditions: - Alphabet followed by number - Repeat character according
to the number - If alphabet is uppercase convert expanded characters
into lowercase - Ignore special symbols - Display expanded string -
Display total character count'''


s=input("enter compressed message")
exp=""
i=0
while i<len(s):
      exp=exp+s[i].lower()*int(s[i+1])
      i=i+2
print("Expanded message",exp)
print("Total Character:",len(exp))
      
