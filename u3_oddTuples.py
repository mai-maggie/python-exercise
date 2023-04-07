def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    # Your Code Here
    if len(aTup) == 0:
        return tuple()
    else:
        newList = list()
        for idx in range(0, len(aTup), 2):
            newList.append(aTup[idx])
        return tuple(newList)


tuple1 = (1, 2, 3)

print(oddTuples(tuple1))
