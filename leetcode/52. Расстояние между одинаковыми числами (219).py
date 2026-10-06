def containsNearbyDuplicate(nums, k):
    #индекс последней встречи каждого числа
    last_index = {}
    #[индекс, число]
    for i, num in enumerate(nums):
        #если это число встречалось
        if num in last_index:
            #проверим расстояние
            if i - last_index[num] <= k:
                return True
        #если оно не подошло
        #обновим последний индекс числа
        last_index[num] = i
    #если никого не нашли
    return False
