def fib(n):
    x = [1, 2]
    if n <= 2:
        return x[end-1]
    else:
        for i in range(2, n):
            x.append(x[i-1]+x[i-2])
        return x

def digits(m):
    return len(str(m))


n = 3
Y = fib(n)
while digits(Y[len(Y)-1]) != 1000:
    n += 1
    Y = fib(n)

print len(Y)+1

