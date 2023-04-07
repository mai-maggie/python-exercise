# way 1
def genPrimes1():
    x = 1
    primeList = []
    while True:
        x += 1
        for num in primeList:
            if (x % num) == 0:
                break
        else:  # for-else clause, when the loop is break, else won't execute
            primeList.append(x)
            yield x


# way 2
def genPrimes2():
    x = 1
    primeList = []
    result = False
    while True:
        if result:
            primeList.append(x)
            yield x
        x += 1
        for num in primeList:
            if (x % num) == 0:
                result = False
                break
        else:
            result = True
