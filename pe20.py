def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)

x = str(factorial(100))
sum = 0
for i in range(0,len(x)):
    sum += int(x[i])
print sum
