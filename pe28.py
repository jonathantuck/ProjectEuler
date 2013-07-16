import time

start = time.time()

sum = 1
count = 0
add = 2
dim = 1001*1001

x = 1

while x < dim:
    count += 1
    x += add
    sum += x
    if count == 4:
        count = 0
        add += 2

print sum

stop = time.time()
print stop-start

#completes in about .00095 seconds.
