array = []
for a in range(2,101):
    for b in range(2,101):
        if not(a**b in array):
            array.append(a**b)
print len(array)
