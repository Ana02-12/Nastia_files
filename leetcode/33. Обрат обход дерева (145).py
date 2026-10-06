def postorderTraversal(root):
    res = []
    # рекурсия -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    # def dfs(node):
    #     if not node: return
    #     dfs(node.left)
    #     dfs(node.right)
    #     res.append(node.val)
    # dfs(root)
    # return res
    #стек -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    stack = [[root, False]]
    while stack:
        node, fl = stack.pop()
        if not node:
            continue
        if fl:
            res.append(node.val)
        else:
            stack.append([node, True])
            if node.right:
                stack.append([node.right, False])
            if node.left:
                stack.append([node.left, False])
    return res

