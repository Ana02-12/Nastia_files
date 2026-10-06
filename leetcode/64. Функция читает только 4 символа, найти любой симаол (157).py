def read(buf, n):
    total = 0

    while total < n:
        buf4 = [''] * 4
        count = read4(buf4)

        # копируем нужное количество символов
        for i in range(min(count, n - total)):
            buf.append(buf4[i])

        total += min(count, n - total)

        # файл закончился
        if count < 4:
            break

    return total

