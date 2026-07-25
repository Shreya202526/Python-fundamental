'''Customer Feedback Analysis System
An e-commerce company receives thousands of customer reviews every day for its products.
To analyze customer opinions efficiently, the analytics team wants a Python program that 
counts how many times each word appears in a review message.
This helps the company identify frequently used words such as:

good
bad
delivery
quality
service

Write a Python program to count the frequency of every word in a given sentence.

Input:33333
delivery was fast and delivery service was good
Output:
delivery : 2
was : 2
fast : 1
and : 1
service : 1
good : 1'''


s=input("Input:")
new_string=s.split()
visited=""
for i in new_string:
    if i not in visited:
         c1=0
         for j in new_string:
           if i==j:
             c1=c1+1
    print(i ,c1)
    visited=visited+i+" "
