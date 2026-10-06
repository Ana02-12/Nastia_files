def addDigits(num: int) -> int:
    #пока число двузначное и более
    while num >= 10:
        total = 0
        #пока не использовали все его разряды
        while num > 0:
            total += num % 10
            num //= 10
        #новое число это сумма разрядов предыдущего
        num = total

    return num
