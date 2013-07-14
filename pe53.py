def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n-1)

def C(n,r):
    return fact(n) / (fact(r) * fact(n-r))

sum = 0
for n in range(23,100+1):
    for r in range(0,n+1):
        if C(n,r) > 10**6:
            sum += 1

print sum
        
