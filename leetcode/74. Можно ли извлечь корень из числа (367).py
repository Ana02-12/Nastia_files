def f(x):
    if x == 1:
        return True

    l, r = 2, x // 2

    while l <= r:
        m = (l + r) // 2
        if m**2 == x:
            return True
        elif m**2 < x:
            l = m + 1
        elif m**2 > x:
            r = m - 1
    return False

print(f(4))