import time

def d(n):
    sum = 0
    for i in range(1,n/2+1):
        if n%i == 0:
            sum += i
    return sum


start = time.time()
sum = 0
bound = 10000
for a in range(1,bound):
    b = d(a)
    if d(b) == a and a != b:
        sum += a
print sum
stop = time.time()

print stop-start
