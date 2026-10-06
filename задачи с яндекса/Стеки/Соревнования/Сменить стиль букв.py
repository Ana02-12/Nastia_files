def main():
    n = int(input())
    #для каждого вводимого слова
    for _ in range(n):
        word = input()
        w = word[0].lower()
        #для каждой буквы
        for i in range(1, len(word)):
            ch = word[i]
            if ch.isupper():
                w += '_' + ch.lower()
            else:
                w += ch
        print(w)


if __name__ == '__main__':
    main()

