def preorderTraversal(root):
    res = []
    #рекурсия -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    # def dfs(node):
    #     if not node: return
    #     res.append(node.val)
    #     dfs(node.left)
    #     dfs(node.right)
    # dfs(root)
    # return res
    #стек -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    if not root: return []
    stack = [root]
    while stack:
        node = stack.pop()
        if not node:
            continue
        res.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res





