import time

def fib(n):
    x = [1, 2]
    if n <= 2:
        return x
    else:
        for i in range(2, n):
            x.append(x[i-1]+x[i-2])
        return x

start = time.time()
y = fib(100)
sum = 0
for j in range(0, len(y)):
    if y[j] < 4*(10**6) and y[j]%2==0:
        sum += y[j]
print sum
stop = time.time()
print str(stop-start) + ' seconds is how long the code took to give a solution.'
