def isHappy(n):
    #поиск суммы квадратов цифр
    def sqr_dig(n):
        sums = 0
        while n > 0:
            sums += (n % 10) ** 2
            n //= 10
        return sums
    sl = sqr_dig(n)
    fs = sqr_dig(sqr_dig(n))
    while True:
        #встретили единицу
        if fs == 1:
            return True
        #указатели встретились
        if sl == fs:
            return False
        sl = sqr_dig(sl)
        fs = sqr_dig(sqr_dig(fs))

#черзе множество -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-
def f(n):

    def sq(n):
        res = 0
        while n > 0:
            last = n % 10
            res += last ** 2
            n //= 10
        return res

    seen = set() #храним все увиденные числа
    while True:
        n = sq(n) #постоянно меняем n
        if n == 1:
            return True
        if n in seen: #начался цикл
            return False

        seen.add(n) #запомним то, что увидели