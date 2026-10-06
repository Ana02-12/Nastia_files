def firstBadVersion(n):
    #версии идут с одного
    left = 1
    #последняя версия
    right = n

    while left < right:
        #вычислим расстояние
        dist = (right - left)

        #пройдем половину расстояния
        mid = left + dist // 2

        #если мы стоим на плохой версии
        if isBadVersion(mid):
            #передвинем правый указатель
            #мы точно знаем, что все
            #правее середины плохие
            right = mid
        else:
            #передвинем указатель дальше середины
            #так как мы ищем именно плохую версию
            left = mid + 1

    return left

