def isSameTree( p, q):
#recursion -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--==-=-=-=
    if not p or not q:
        return p == q

    return p.val == q.val and \
           isSameTree(p.left, q.left) and \
           isSameTree(p.right, q.right)
#stack -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--==-=-=-=-=-=
def isSameTree(p, q):
    stack = [(p, q)]

    while stack:
        n1, n2 = stack.pop()

        # оба узла пустые
        if not n1 and not n2:
            continue

        # один пустой, другой нет
        if not n1 or not n2:
            return False

        # значения отличаются
        if n1.val != n2.val:
            return False

        # добавляем детей для дальнейшей проверки
        stack.append((n1.left, n2.left))
        stack.append((n1.right, n2.right))

    return True