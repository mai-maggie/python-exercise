def genPrimes():
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


foo = genPrimes()
print(next(foo))
print(next(foo))
print(next(foo))
