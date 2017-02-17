import sys


T = int(raw_input().strip())

for i in range (T):
    s = raw_input().strip()
    o = ""
    e = ""
    for j in range(len(s)):
        if j%2 == 0:
            e = e + s[j]
        else:
            o = o + s[j]
    print e, o

#Objective 
#Today we're expanding our knowledge of Strings and combining it with what we've already learned about loops. Check out the Tutorial tab for learning materials and an instructional video!
#Task 
#Given a string, , of length  that is indexed from  to , print its even-indexed and odd-indexed characters as  space-separated strings on a single line (see the Sample below for more detail).
#Note:  is considered to be an even index.
#Input Format
#The first line contains an integer,  (the number of test cases). 
#Each line  of the  subsequent lines contain a String, .
#Constraints
#•	
#•	
#Output Format
#For each String  (where ), print 's even-indexed characters, followed by a space, followed by 's odd-indexed characters.
#Sample Input
#2
#Hacker
#Rank
#Sample Output
#Hce akr
#Rn ak
