import math
import time

def sumFact(x):
    x = str(x)
    ans = 0
    for i in range(0,len(x)):
        ans += math.factorial(int(x[i]))
    return ans

startTime = time.time()
sum = 0
bound = 100000
for j in range(3,bound):
    if j == sumFact(j):
        sum += j

print sum

stopTime = time.time()
print stopTime-startTime
