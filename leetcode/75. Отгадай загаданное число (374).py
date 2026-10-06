#guess возвращает 1 или -1

def f(n):
    l, r = 1, n
    while l <= r:
        m = (l + r) // 2
        ans = guess(m)
        if ans == 0:
            return m
        elif ans == -1:
            r = m - 1
        elif ans == 1:
            l = m + 1


