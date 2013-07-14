import time

start = time.time()
prod = 1
bound = 1000
for c in range(1,bound):
    for b in range(1,bound-1):
        for a in range(1,bound-2):
            if a+b+c==1000 and a**2+b**2==c**2:
                prod = a*b*c
print prod

stop = time.time()
print stop-start
