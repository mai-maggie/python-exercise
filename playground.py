def genPrimes():
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


foo = genPrimes()
print(next(foo))
print(next(foo))
