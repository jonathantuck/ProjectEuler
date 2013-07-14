import math
import time

def isPrime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x%i == 0:
            return False
    return True

start = time.time()
count,i = 0,1
bound = 10001
while count < bound:
    i += 1
    if isPrime(i):
        count += 1
    
print i
stop = time.time()
print stop-start
