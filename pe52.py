import time


bound = 10**7
for x in range(1,bound):
    x = sorted(list(str(x)))
    if x == sorted(list(str(6*x))):
        if x == sorted(list(str(5*x))):
            if x == sorted(list(str(4*x))):
                if x == sorted(list(str(3*x))):
                    if x == sorted(list(str(2*x))):
                        print x
