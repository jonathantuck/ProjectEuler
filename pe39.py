import time

start = time.time()

bound = 1000
count = 0
ans = 0
for p in range(1,bound+1):
    print p
    internalcount = 0
    for a in range(1,p/2):
        for b in range(1,p/2):
            for c in range(1,p/2):
                if (a+b+c==p) and (a**2+b**2==c**2):
                    internalcount += 1
    if internalcount > count:
        count = internalcount
        ans = p

print ans

stop = time.time()
print stop-start
