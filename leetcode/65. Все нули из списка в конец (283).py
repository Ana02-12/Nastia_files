def f(n):
    l = 0
    for r in range(len(n)):
        #ищем не ноль
        if n[r] != 0:
            #меняем его местами с l
            n[l], n[r] = n[r], n[l]
            #двигаем l
            l += 1
