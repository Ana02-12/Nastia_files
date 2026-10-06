def infix_to_post(s):
    priority = {
        '+': 1,
        '-': 1,
        '*': 2
    }

    stack = []  #операции
    result = [] #числа

    for x in s:
        #если это число -=-=-=-=-=-=-=-=-=-=-=-=-=-=
        if x.isdigit():
            result.append(x)

        #открывающая скобка -=-=-=-=-=-=-=-=-=-=-=-=
        elif x == '(':
            stack.append(x)

        #закрывающая скобка -=-=-=-=-=-=-=-=-=-=-=-=
        elif x == ')':
            #найти скобку и убрать её
            while stack[-1] != '(':
                #записать все операции до скобки
                last = stack.pop()
                result.append(last)
            #убрать найденную скобку
            stack.pop()

        #операция -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        else:
            #стек не пустой
            #до нас была не скобка
            #до нас была операция с большим либо
            #равным приоритетом
            while (stack and stack[-1] != '(' and
                   priority[stack[-1]] >= priority[x]):
                #запишем старшую операцию
                result.append(stack.pop())

            #когда все старшие операции обработаны
            #кладем текущую в стек
            stack.append(x)
    #заберем из стека всё что осталось -=-=-=-=-=-=-=-=
    while stack:
        result.append(stack.pop())

    return ' '.join(result)