def binaryTreePaths(self, root):
    result = []

    def dfs(node, path):
        if not node:
            return

        path += str(node.val)

        # если дошли до листа
        if not node.left and not node.right:
            result.append(path)
            return

        path += "->"

        dfs(node.left, path)
        dfs(node.right, path)

    dfs(root, "")

    return result

