def post_count():
    s = input().split()

    stack = []

    for ch in s:

        #если это число
        if ch not in '+-*':
            stack.append(int(ch))

        #если это операция произведем её
        #над последними из стека
        else:
            b = stack.pop()
            a = stack.pop()

            if ch == '+':
                stack.append(a + b)
            elif ch == '-':
                stack.append(a - b)
            else:
                stack.append(a * b)

    print(stack[0])
