import math

a = 3.3
b = 10 
c = 2

x1 = 0.0
x2 = 0.0


if (a == 0):
    print ("Error: a=0")
elif ((4 * a * c) > (b*b)):
    print ("Error: 4ac > b*b")
else:
    x1 = (-b + math.sqrt((b*b) - (4 * a * c))) / (2 * a)
    x2 = (-b - math.sqrt((b*b) - (4 * a * c))) / (2 * a)
    print (x1)
    print (x2)
