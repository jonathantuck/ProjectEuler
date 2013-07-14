import time

def collatz(n,terms):
    if n==1:
        return terms
    if n%2==0:
        return collatz(n/2,terms+1)
    if n%2 != 0:
        return collatz(1+3*n,terms+1)



largestTerms = 0
startNum = 0
for k in range(1,10**6):
    if collatz(k,1) > largestTerms:
        largestTerms = collatz(k,1)
        startNum = k
print startNum
