def climbstairs(n):
    if n == 0: return 0
    if n <= 2: return n
    l = 1
    r = 2
    for _ in range(3, n + 1):
        cur = l + r
        l = r
        r = cur
    return r
