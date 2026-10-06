import sys
import random
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-
#переставляем элементы и возвращаем начало второй части
def partition(a, left, right, x):
    i = left
    j = right

    #ищем элементы, которые стоят не на своем месте
    while i <= j:
        #пока не найдем слева кого-то больше х
        while a[i] < x:
            i += 1

        #пока не найдем справа кого-то больше х
        while a[j] > x:
            j -= 1

        #двигаем элементы только если они
        #не пересеклись
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1

    #возвращаем начало правой части
    return i

#сортировка -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def quick_sort(a, left, right):
    #пока в рассматриваемой части есть
    #хотя бы два элемента
    while left < right:
        #опорный элемент, лучше случайный
        x = a[random.randint(left, right)]

        split = partition(a, left, right, x)

        if split - left < right - split + 1:
            quick_sort(a, left, split - 1)
            left = split
        else:
            quick_sort(a, split, right)
            right = split - 1


def main():
    n = int(input())
    a = [int(x) for x in input().split()]

    if n > 1:
        quick_sort(a, 0, n - 1)

    print(*a)


if __name__ == '__main__':
    main()