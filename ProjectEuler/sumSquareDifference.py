def sumOfSquares(upTo):
    sum = 0
    for x in range(1,upTo+1):
        sum += x **2
    return sum

def squareOfSum(upTo):
    sum = 0
    for x in range(1,upTo+1):
        sum += x
    sum = sum**2
    return sum

print(squareOfSum(100)-sumOfSquares(100))