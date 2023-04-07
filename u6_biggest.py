def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    if len(aDict) == 0:
        return None
    elif len(aDict) == 1:
        return list(aDict.keys())[0]
    else:
        findBigAnimal = list(aDict.keys())[0]
        valuesList = list(aDict.values())
        for idx, item in enumerate(valuesList):
            if idx + 1 < len(aDict):
                if len(valuesList[idx]) <= len(valuesList[idx + 1]):
                    findBigAnimal = list(aDict.keys())[idx + 1]
        return findBigAnimal


animals = {'a': [15, 2], 'c': [18, 13, 10, 11, 10], 'b': [7, 3, 14, 1, 18, 5, 13, 10, 2, 11], 'd': [18]}
print(biggest(animals))
