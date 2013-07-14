import time

start = time.time()

sum = 0
f = open('numlist_pe13.txt','r')
for line in f:
    sum += int(line)

print str(sum)[0:10]

stop = time.time()

print stop-start
