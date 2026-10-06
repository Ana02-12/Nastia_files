def isSymmetric(root):
#recursion -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--==-=-=-=
    def is_mirror(n1, n2):  # n1:left, n2:right
        if not n1 and not n2:
            return True

        if not n1 or not n2:
            return False

        return n1.val == n2.val and \
            is_mirror(n1.left, n2.right) and \
            is_mirror(n1.right, n2.left)

    return is_mirror(root.left, root.right)
#stack -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--==-=-=-=-=-=
def isSymmetric(root):
    if not root:
        return True

    stack = [[root.left, root.right]]

    while stack:
        left, right = stack.pop()

        # оба пустые — эта пара симметрична
        if not left and not right:
            continue

        # один пустой, другой нет — нарушение симметрии
        if not left or not right:
            return False

        # значения не совпадают
        if left.val != right.val:
            return False

        # добавляем зеркальные пары детей
        stack.append([left.left, right.right])
        stack.append([left.right, right.left])

    return True