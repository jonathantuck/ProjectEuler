import time
def rot(str,n):
    return str[n:] + str[:n]

def isPrime(x):
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True

start = time.time()

sum = 0
bound = 10**6
for i in range(2,bound):
    if isPrime(i):
        count = 0
        for j in range(0,len(str(i))):
            if isPrime(int(rot(str(i),j))):
                count += 1
        if count == len(str(i)):
            sum += 1
print sum

stop = time.time()
print stop-start
