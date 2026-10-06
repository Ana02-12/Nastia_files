#найдем элементы, которые меньше опорного элемента
def partition(a, x):
    count = 0

    for value in a:
        if value < x:
            count += 1

    return count

#выведем элементы меньше и больше\равно х
def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    x = int(input())

    left = partition(a, x)
    right = n - left

    print(left)
    print(right)


if __name__ == '__main__':
    main()