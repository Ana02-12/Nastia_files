def f(n1, len_n1, n2, len_n2):
    r = (len_n1 + len_n2) - 1
    p1 = len_n1 - 1
    p2 = len_n2 - 1
    while p1 >= 0 and p2 >= 0:
        if n1[p1] > n2[p2]:
            n1[r] = n1[p1]
            p1 -= 1
        else:
            n1[r] = n2[p2]
            p2 -= 1
        r -= 1
    while p2 >= 0:
        n1[r] = n2[p2]
        p2 -= 1
        r -= 1
    return n1
l1 = [7, 8, 0, 0]
l2 = [1, 2]
print(f([7, 2, 0, 0, 0, 0], 2, [1, 2, 3, 4], 4))