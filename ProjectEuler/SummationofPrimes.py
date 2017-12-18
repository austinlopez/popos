import math
import time
start_time = time.time()

def isPrime(num):
    for i in range(2,int(num/2)):
        if num % i == 0:
            return False
    return True

def addPrimes(upTo):
    sumOfPrimes = 0
    primes = [2,3]
    for x in range(5,upTo + 1):
        if isPrime(x):
            sumOfPrimes += x
            primes.append(x)
            print(x, time.time()-start_time)
    print(primes)
    return sumOfPrimes

print(addPrimes(100))
print("It took", time.time()-start_time,"seconds to run")