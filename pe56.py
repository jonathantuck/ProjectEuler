def DigitSum(x):
    sum = 0
    x = str(x)
    for i in range(0,len(x)):
        sum += int(x[i])
    return sum

largest = 0
for a in range(1,100):
    for b in range(1,100):
        if DigitSum(a**b) > largest:
            largest = DigitSum(a**b)

print largest
