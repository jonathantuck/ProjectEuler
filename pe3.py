import math
import time

def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

start = time.time()

x = 600851475143

primelist = []
n = 1

while x != 1:
    n += 1
    if x%n == 0 and isPrime(n):
        primelist.append(n)
        x = x/n
        n = 1
print max(primelist)

stop = time.time()

print stop-start
