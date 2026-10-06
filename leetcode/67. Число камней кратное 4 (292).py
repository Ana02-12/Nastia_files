# def f(n):
#     if n % 4 == 0:
#         return False
#     return True

#рекурсия с мемоизацией -=-=-=-=-=-=-=-=-=-=-=-=-==-=
def f(n, memo = {}):
    if n <= 3:
        return True

    if n in memo:
        return memo[n]

    one = f(n-1, memo)
    two = f(n-2, memo)
    three = f(n-3, memo)

    memo[n] = (not one or not two or not three)

    return memo[n]


