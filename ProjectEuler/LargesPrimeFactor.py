import math
#testNumber = 13195
testNumber = 600851475143

def isPrime(num):
    for i in range(2,int(num/2)):
        if num % i == 0:
            return False
    return True

def largestPrimeFactor(num):
    rest = num
    i = 1
    while rest != 1:
        i += 1
        if isPrime(i) and rest % i == 0:
            rest = rest / i
    return i

print(largestPrimeFactor(testNumber))



'''
prime = []
#testNumber = 13195
testNumber = 600851475143
primeFactors = []
sqrtTest = math.sqrt(testNumber)
print(sqrtTest)

for x in range(int(sqrtTest),2,-1):
    times = 0
    for y in range(2,int(sqrtTest)):
        if x % y == 0 :
            times += 1
            #print(x)
    if times == 1:
        #prime.append(x)
        if testNumber%x == 0:
            print(x)
            break
        #print(x)

# for x in prime:
#     if testNumber%x == 0:
#         primeFactors.append(x)

#print(dontTest[0])
'''

'''
for x in range(int(testNumber/2),1,-1):
    if testNumber%x == 0:
        for div in range(x,2,-1):
            if x % div ==0:
                pass
            else:
                prime.append(x)
                break
'''
#print(prime)
#print(dontTest)