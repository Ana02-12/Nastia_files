def tokenize(s):  # разбиение на токены =========================
    tokens = []
    i = 0 #текущая позиция
    lens = len(s) #все позиции

    while i < lens:
        cur = s[i]

        #если пробел идем дальше -=-=-=-=-=-=-=-=-=-=-=
        if cur == ' ':
            i += 1

        #если цифра -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        elif cur.isdigit():
            j = i #конец числа
            #пока не прошли всю строку и
            #пока встречаем цифры
            while j < lens and s[j].isdigit():
                j += 1
            tokens.append(s[i:j])  #число целиком
            i = j #первое неподходящее наше новое начало

        #если операция -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        elif cur in '+-*()':
            tokens.append(cur)
            i += 1
        #если недопустимый символ -=-=-=-=-=-=-=-=-=-=-=-=-
        else:
            tokens.append(None)
            i += 1

    return tokens


def is_valid(tokens):  #валидность ============================
    balance = 0 #счетчик скобок
    need = 'value' #ожидаем увидеть

    for tok in tokens:
        #недопустимое значение
        if tok is None:
            return False

        #число или '('
        if need == 'value':
            #число
            if tok.isdigit():
                #теперь ждем оператор или ')'
                need = 'operator'
            #скобка
            elif tok == '(':
                balance += 1 #запишем её
                #также ждем число или '('
            #получили не то, что ждали
            else:
                return False

        #ждем оператор или ')'
        else:
            #если оператор ждем значение или '('
            if tok in '+-*':
                need = 'value'
            #если ')' ждем оператор или еще одну ')'
            elif tok == ')':
                balance -= 1
                if balance < 0:
                    return False
            #получили не то, что ждали
            else:
                return False
    #больше не ждем значения и скобки в балансе
    return need == 'operator' and balance == 0


def infix_to_postfix(tokens):  # перевод =========================
    priority = {
        '+': 1,
        '-': 1,
        '*': 2
    }

    stack = []
    result = []

    for tok in tokens:
        if tok.isdigit():
            result.append(tok)

        elif tok == '(':
            stack.append(tok)

        elif tok == ')':
            while stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()

        else:
            while (stack and stack[-1] != '(' and
                   priority[stack[-1]] >= priority[tok]):
                result.append(stack.pop())
            stack.append(tok)

    while stack:
        result.append(stack.pop())

    return result


def evaluate_postfix(postfix):  # подсчет ========================
    stack = []

    for tok in postfix:
        if tok.isdigit():
            stack.append(int(tok))
        else:
            b = stack.pop()
            a = stack.pop()

            if tok == '+':
                stack.append(a + b)
            elif tok == '-':
                stack.append(a - b)
            else:
                stack.append(a * b)

    return stack[0]


def main():
    s = input()
    #разделим на части
    tokens = tokenize(s)

    #проверим валидность
    if is_valid(tokens):
        postfix = infix_to_postfix(tokens)
        print(evaluate_postfix(postfix))
    else:
        print('WRONG')


if __name__ == '__main__':
    main()
