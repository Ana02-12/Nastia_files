from collections import deque


def main():
    first = deque(map(int, input().split()))
    second = deque(map(int, input().split()))

    for moves in range(1, 10**6+1):
        #достаем слева
        a = first.popleft()
        b = second.popleft()

        #первый выиграл
        if a == 0 and b == 9 \
                or a > b and not (a == 9 and b == 0):
            first.append(a)
            first.append(b)
        #второй выиграл
        else:
            second.append(a)
            second.append(b)

        #карты кончились у одного из них
        if not first:
            print("second", moves)
            return

        if not second:
            print("first", moves)
            return

    print("botva")


if __name__ == '__main__':
    main()
