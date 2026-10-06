n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

answer = 0

#строка
for i in range((n + 1) // 2):
    #столбец
    for j in range((m + 1) // 2):

        #убираем повторяющиеся координаты,
        #если они встретились в центре
        positions = {
            #она сама
            (i, j),
            #правый верх
            (i, m - 1 - j),
            #левый низ
            (n - 1 - i, j),
            #правый низ
            (n - 1 - i, m - 1 - j)
        }

        values = [matrix[x][y] for x, y in positions]

        max_count = max(values.count(x) for x in values)

        answer += len(values) - max_count

print(answer)


