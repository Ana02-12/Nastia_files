#рекурсия -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def dfs(node):
    if not node:
        return 0

    left = dfs(node.left)
    right = dfs(node.right)

    if not node.left:
        return right + 1

    if not node.right:
        return left + 1

    return 1 + min(left, right)

#стек -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def minDepth(root):
    if not root:
        return 0

    stack = [(root, 1)]
    ans = float("inf")

    while stack:
        node, depth = stack.pop()

        if not node.left and not node.right:
            ans = min(ans, depth)

        if node.left:
            stack.append((node.left, depth + 1))

        if node.right:
            stack.append((node.right, depth + 1))

    return ans



