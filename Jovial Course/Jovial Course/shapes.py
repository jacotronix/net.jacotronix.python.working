import math

pi = math.pi

testdata = [["SPH", 0, 0, 0, 0, 0],
            ["CUB", 0, 0, 0, 0, 0],
            ["REC", 0, 0, 0, 0, 0],
            ["CYL", 0, 0, 0, 0, 0],
            ["PYR", 0, 0, 0, 0, 0],
            ["CON", 0, 0, 0, 0, 0]]


# sphere - v = 4/3 * pi * r*r
def calcVSphere(radius):
    return ((4/3) * pi * (radius * radius))

# cube = v = s * s * s
def calcVCube(side):
    return (side * side * side)

# retangular solid - v = l * w * h
def calcVRectangle(len, wid, hi):
    return (len * wid * hi)

# cylinder - v = pi * r*r * h
def calcVCylinder(rad, hi):
    return (pi * (rad * rad) * hi)

# pyramid - v = 1/3 * A * h, where A = l * w 
def calcVPyramid(h, l, w):
    bottomArea = l * w
    return ((1/3) * bottomArea * h)

# cone - v = 1/3 * pi * r*r * h
def calcVCone(r, h):
    return ((1/3) * pi * (r*r) * h)

for record in range(0, 10):
    if testdata[record][0] == "SPH":
        print testdata[record]
    elif testdata[record][0] == "CUB":
        print testdata[record]
    elif testdata[record][0] == "REC":
        print testdata[record]
    elif testdata[record][0] == "CYL":
        print testdata[record]
    elif testdata[record][0] == "PYR":
        print testdata[record]
    elif testdata[record][0] == "CON":
        print testdata[record]
