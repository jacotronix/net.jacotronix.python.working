#Given a time in -hour AM/PM format, convert it to military (-hour) time.
#Note: Midnight is  on a -hour clock, and  on a -hour clock. Noon is  on a -hour clock, and  on a -hour clock.
#Input Format
#A single string containing a time in -hour clock format (i.e.:  or ), where  and .
#Output Format
#Convert and print the given time in -hour format, where.
#Sample Input
#07:05:45PM
#Sample Output
#19:05:45

time = raw_input().strip()

hour = int(time[0:2])
op = time[:8]
if time[8] == "P":
    if hour < 12:
        hour += 12
    op = str(hour) + op[2:]
elif hour == 12:
    op = "00" + op[2:]
print op
