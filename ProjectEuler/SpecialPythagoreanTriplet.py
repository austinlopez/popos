import math

def isTriplet(a,b):
    a2 = a**2
    b2 = b**2
    c2 = a2+b2
    c = math.sqrt(c2)
    if c.is_integer():
        return True
    return False

def checkFor1000(a,b,equal):
    c = math.sqrt(a**2 + b**2)
    sum = a+b+c
    if sum == equal:
        return True
    return False

def findTripletProduct(num):
    b = 2
    number = 2
    while True:
        for a in range(b):
            if isTriplet(a,b) and checkFor1000(a,b,num):
                return (a*b*(int(math.sqrt(a**2 + b**2))),a,b,(int(math.sqrt(a**2 + b**2))))
        b += 1


print(findTripletProduct(1000))