def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''

    # Your Code Here
    def flatten_list(alist, result):
        if type(alist) == list:
            for item in alist:
                if type(item) == list:
                    return flatten_list(item, result)
                else:
                    result.append(item)
        else:
            result.append(alist)
        return result

    values_list = []
    result = []
    for a in aDict.values():
        values_list = flatten_list(a, result)
    return len(values_list)


dic1 = {1: [1, 2, 3], 2: [4, 7, 2], 3: [43, [5, 2, [5, 7]]]}
print(how_many(dic1))
