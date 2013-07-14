def chain(x):
    if x==1 or x==89:
        return x
    x = str(x)
    sum = 0
    for i in range(0,len(x)):
        sum += int(x[i])**2
    return chain(sum)


count = 0
bound = 10**7
for j in range(1,bound):
    if chain(j)==89:
        count += 1

print count

