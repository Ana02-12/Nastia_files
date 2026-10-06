#разделить на токены ===============================
def tokenize(s):
    tokens = []
    for ch in s:
        if ch in '01':
            tokens.append(int(ch))
        else:
            tokens.append(ch)

    return tokens
#перевести в постфиксную запись =========================
def infix_to_postfix(tokens):
    priority = {
        '!': 3,
        '&': 2,
        '|': 1,
        '^': 1
    }

    stack = []
    result = []

    for tok in tokens:
        #если это число
        if tok in (0, 1):
            result.append(tok)

        elif tok == '(':
            stack.append(tok)

        #если скобка закрылась
        #запишем все операции внутри
        elif tok == ')':
            while stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()

        elif tok == '!':
            stack.append(tok)

        #если это операция
        #сначала выполним все с приоритетом выше
        #после добавим её саму в стек
        else:
            while stack and \
                    stack[-1] != '(' and \
                    priority[stack[-1]] >= priority[tok]:
                result.append(stack.pop())

            stack.append(tok)

    #достанем всё что осталось из стека
    while stack:
        result.append(stack.pop())

    return result

#вычисление =============================================
def calculate(postfix):
    stack = []

    for tok in postfix:
        if tok in (0, 1):
            stack.append(tok)

        elif tok == '!':
            a = stack.pop()
            stack.append(1 - a)

        else:
            b = stack.pop()
            a = stack.pop()

            if tok == '&':
                stack.append(a & b)
            elif tok == '|':
                stack.append(a | b)
            elif tok == '^':
                stack.append(a ^ b)

    return stack[0]
#главная функция =======================================
def main():
    s = input()

    tokens = tokenize(s)
    postfix = infix_to_postfix(tokens)
    answer = calculate(postfix)

    print(answer)

if __name__ == '__main__':
    main()