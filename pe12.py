import time

def tri(a):
    return sum(list(xrange(a+1)))

def div(b):
    count = 1
    # count is initialized at 1 to account for b being a factor of b.
    for n in range(1, b/2 + 1):
        if b%n == 0:
            count += 1
    return count

start = time.time()

num = False
j = 4990
while (not num):
    print tri(j)
    j += 1
    if div(tri(j)) > 500:
        num = True
        print tri(j)

stop = time.time()
print stop-start
