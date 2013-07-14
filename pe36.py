import time

def isPalindBIN(x):
    x = str(x[2:len(x)])
    return x == x[::-1]

def isPalindDEC(x):
    x = str(x)
    return x == x[::-1]

bound = 10**6
sum = 0
for i in range(1,bound):
    if isPalindBIN(bin(i)) and isPalindDEC(i):
        sum += i

print sum
