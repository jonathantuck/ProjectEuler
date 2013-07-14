import math
import time

def sumPower(x):
    x = str(x)
    n = 5
    ans = 0
    for i in range(0,len(x)):
        ans += int(x[i])**n
    return int(ans)


startTime = time.time()

sum = 0
bound = 10**6
for y in range(2,bound):
    if y==sumPower(y):
        sum += y
print sum

stopTime = time.time()
print stopTime - startTime
