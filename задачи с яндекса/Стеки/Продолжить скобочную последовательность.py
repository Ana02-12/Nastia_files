def main():
    n = int(input()) #кол-во строк
    w = input() #цена символа
    s = input() #начало строки

    pair = {
        '(': ')',
        '[': ']'
    }

    #собрать стек для заданного начала -=-=-=-=-=-=-=-=
    stack = []
    for ch in s:
        if ch in pair:
            stack.append(ch)
        else:
            stack.pop()

    #ответ
    ans = s
    #вычтим уже имеющиеся символы
    n -= len(s)

    #начинаем выбор -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    while n > 0:
        #всегда берем самый маленький
        for ch in w:
            #можем ли открыть?
            if ch in pair:
                #открыли значит мест стало меньше
                #нужно закрыть все, что имеем и
                #еще одну новую
                if n - 1 >= len(stack) + 1:
                    ans += ch
                    stack.append(ch)
                    n -= 1
                    break
            #можем ли закрыть?
            else:
                #есть, что закрывать
                #закрываем по соответсвию
                if stack and pair[stack[-1]] == ch:
                    stack.pop()
                    ans += ch
                    n -= 1
                    break
    print(ans)

main()


