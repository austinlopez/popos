import time
start_time = time.time()

def isDivisible(upTo,num):
    for x in range(1,upTo+1):
        if num % x != 0:
            return False
    return True


def findSmallestMultiple(firstHowMany):
    testNum = 1
    while True:
        if isDivisible(firstHowMany,testNum):
            return testNum
        testNum += 1


if __name__ == '__main__':
    print(findSmallestMultiple(20))
    print("My program took", time.time() - start_time,"to run")