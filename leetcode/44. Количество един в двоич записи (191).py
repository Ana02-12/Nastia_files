def hammingWeight(n: int) -> int:
# -==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#     cnt = 0
#     while n > 0:
#         #последний бит числа
#         last = n & 1
#         #если он единица
#         if last == 1:
#             cnt += 1
#         #убрать последний бит
#         n = n >> 1
#     return cnt
# print(hammingWeight(3))
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    cnt = 0
    while n > 0:
        #вычтем единицу из числа
        previous = n - 1
        #избавляемся от первой единицы с конца
        n = n & previous
        cnt += 1
    return cnt
print(bin(5))

