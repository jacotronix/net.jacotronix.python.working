import math

pi = math.pi



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
