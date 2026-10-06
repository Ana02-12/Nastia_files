def f(nums):
    res = []
    if not nums:
        return res

    start = nums[0]
    for i in range(1, len(nums)):
        #будем смотреть на текущее и предыдущее число
        cur = nums[i]
        prev = nums[i-1]
        #если диапазон разорван
        #текущее число не входит в диапазон
        #prev это последнее число входящее в диапазон
        if cur - prev != 1:
            #если мы не сдвинулись с места
            if start == prev:
                res.append(f'{start}')
            #если сдвинулись
            else:
                res.append(f"{start}->{prev}")
            #начнем новый диапазон
            #с текущего числа, что нарушило его
            start = nums[i]

    #добавляем последний диапазон
    #если не сдвинулись
    if start == nums[-1]:
        res.append(f'{start}')
    #сдвинулись
    else:
        res.append(f"{start}->{nums[-1]}")

    return res