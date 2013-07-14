def isPalind(x):
    x = list(str(x))
    return x == x[::-1]

largest = 0
for x in range(100,1000):
    for y in range(100,1000):
        if (isPalind(x*y) and x*y > largest):
            largest = x*y

print largest
