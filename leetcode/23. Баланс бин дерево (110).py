class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#рекусия -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def isBalanced(self, root) -> bool:
    def dfs(node):
        if not node:
            return 0

        left = dfs(node.left)
        if left == -1:
            return -1

        right = dfs(node.right)
        if right == -1:
            return -1

        if abs(left - right) > 1:
            return -1

        return 1 + max(left, right)
    return dfs(root) != -1
#стек -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def isBalanced(root):
    if not root:
        return True

    stack = [(root, False)]
    height = {}

    while stack:
        node, visited = stack.pop()

        if not node:
            continue

        if not visited:
            stack.append((node, True))
            stack.append((node.right, False))
            stack.append((node.left, False))
        else:
            left = height.get(node.left, 0)
            right = height.get(node.right, 0)

            if abs(left - right) > 1:
                return False

            height[node] = 1 + max(left, right)

    return True
