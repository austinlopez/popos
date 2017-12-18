import math
stopNumber = 100
isP = True
for num in range(2,stopNumber):
    isP = True
    for pCheck in range(2, int(math.sqrt(num))+1):
        if num % pCheck == 0:
            isP = False
    if isP == True:
        print("Found One:",num)