import math


def polysum(n, s):
    """
    :param n: number of sides
    :param s: each side has length of s
    :return: the sum of the area and square of the perimeter of the regular polygon
    """
    area = 0.25 * n * s ** 2 / math.tan(math.pi / n)
    perimeter = math.pow((n * s), 2)
    # round up the sum to 4 decimal places
    sum = round(area + perimeter, 4)
    return sum
