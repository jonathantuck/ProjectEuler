import math

def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True


x = 600851475143

primelist = []
n = 2
while x != 1:
    for i in range(2,x):
        if isPrime(i) and x%i==0:
            primelist.append(i)
            x = x/i
print primelist
    
