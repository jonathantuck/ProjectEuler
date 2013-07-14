import math
import time

def isPrime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x%i == 0:
            return False
    return True


start = time.time()
sum = 0
bound = 2 * (10**6)
for i in range(2,bound):
    print i
    if isPrime(i):
        sum += i

print sum

print time.time()-start
