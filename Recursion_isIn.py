def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''

    # Your code here
    if aStr == '':
        return False
    middle_idx = round(len(aStr) - 1)
    if char == aStr[middle_idx]:
        return True
    elif char > aStr[middle_idx]:
        if middle_idx + 1 < len(aStr):
            return isIn(char, aStr[middle_idx + 1:])
        else:
            return False
    elif char < aStr[middle_idx]:
        if middle_idx >= 0:
            return isIn(char, aStr[0:middle_idx])


print(isIn('e', 'abcd'))
