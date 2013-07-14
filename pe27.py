import math
import time

def isPrime(x):
    for i in range(2,int(abs(x)**0.5)+1):
        if x%i==0:
            return False
    return True

nLargest = 0
prod = 0

for a in range(-999,1000):
    print a
    for b in range(-999,1000):
        n = 0
        y = 3
        while isPrime(y):
            n += 1
            y = int(n**2+a*n+b)
        if n > nLargest:
            prod = a*b
print prod
