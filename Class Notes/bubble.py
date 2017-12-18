#simple implementation of bubble sort
#numberList = [16,18,2,43,6,13,5,9,8,13]
#numberList = [9,1,5,2,2,5,7,11,2,23,12,16,17,19,24,26,27,27,29]
f = open("number.txt", 'r')
fileNumberList = f.read().splitlines()
numberList = []
count = 0
print(fileNumberList)
print(len(fileNumberList))
for x in fileNumberList:
    numberList += x
    count += 1
print(numberList)
f.close


def bubbleSort(numList):
    stillNeedsToSort = True
    loopRan = 0
    innerLoopRan = 0
    while stillNeedsToSort:
        foundOne = False
        for i in range(0,len(numList)-1):
            if numList[i+1] < numList[i]:
                temp = numList[i]
                numList[i] = numList[i + 1]
                numList[i + 1] = temp 
                foundOne = True
            innerLoopRan += 1
        loopRan += 1
        if foundOne == False:
            stillNeedsToSort = False
    print("outer loop ran: ", loopRan)
    print("inner loop ran: ", innerLoopRan)
    return numList
print(len(numberList))
print("Start List", numberList)
print("SortedList", bubbleSort(numberList))