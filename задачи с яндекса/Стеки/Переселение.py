def main():
    n = int(input())
    cities = list(map(int, input().split()))

    ans = [-1] * n
    stack = []

    for i in range(n):
        cur = cities[i]
        #текущее число меньше какого-то
        #из тех, что мы уже видели?
        while stack and cur < cities[stack[-1]]:
            #сразу его забираем
            #так как нам нужен ближайщий
            last = stack.pop()
            #ответ для него найден
            ans[last] = i
        stack.append(i)

    print(*ans)


if __name__ == '__main__':
    main()