import math

testdata = [[0.0, -1.0, 0.0, 0.0, 0.0],
          [-1.0, 0.0, 0.0, 0.0, 0.0],
          [1.0, 0.0, 0.0, 0.0, 0.0],
          [0.0, 1.0, 0.0, 0.0, 0.0],
          [3500.0, 3501.0, 0.0, 0.0, 0.0],
          [-5.0, 5.0, 0.0, 0.0, 0.0],
          [5.0, -5.0, 0.0, 0.0, 0.0],
          [-5.0, -5.0, 0.0, 0.0, 0.0],
          [5.0, 5.0, 0.0, 0.0, 0.0],
          [0.0, 0.0, 0.0, 0.0, 0.0]]

walkingSpeed = 5.0 #mph

def calcRange(x, y):
    return math.sqrt((x*x)+(y*y))

def calcHeading(x, y):
    if (x == 0):
        if (y > 0):
            return 0.0
        else:
            return 180.0

    if (y == 0):
        if (x > 0):
            return 90.0
        else:
            return 270.0

    theta = abs(math.degrees(math.atan(y/x)))

    if (x > 0):
        if (y > 0):
            return 90.0 - theta
        else:
            return 90.0 + theta
    elif (x < 0):
        if (y > 0):
            return 360.0 - theta
        else:
            return 270.0 - theta
        

def calcTime(distance, speed):
    return distance / (speed / 60)

for record in range(0, 9):
    testdata[record][2] = calcRange(testdata[record][0], testdata[record][1])
    testdata[record][3] = calcHeading(testdata[record][0], testdata[record][1])
    testdata[record][4] = calcTime(testdata[record][2], walkingSpeed)
    print (testdata[record])
