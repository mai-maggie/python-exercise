def ggb():
    x = abs(num)
    y = abs(denom)
    while x:
        x, y = y % x, x
    factor = y
