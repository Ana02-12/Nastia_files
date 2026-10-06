#кол-во цифр
#таргет, который нельзя получать
n, k = map(int, input().split())

cnt = {}
nums = list(map(int, input().split()))
#посчитаем кол-во вхождений каждого числа
for num in nums:
    cnt[num] = cnt.get(num, 0) + 1

ans = 0 #сколько чисел нужно удалить
#для каждого значения в словаре
for num in cnt:
    #рассматриваем числа только меньше k/2
    if num <= (k - 1) // 2:
        #уберем число с мин кол-во вхождений
        ans += min(cnt[num], cnt.get(k - num, 0))
#рассмотрим случай, когда k четное
if k % 2 == 0 and k // 2 in cnt:
    #уберем все числа, оставим одно
    ans += cnt[k // 2] - 1
print(ans)
 
