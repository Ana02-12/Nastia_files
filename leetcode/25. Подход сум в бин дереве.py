#рекурсия -=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def hasPathSum(root, targetSum):
    if not root:
        return False

    if not root.left and not root.right:
        return targetSum == root.val

    targetSum -= root.val

    return (hasPathSum(root.left, targetSum) or
            hasPathSum(root.right, targetSum))
#стек -=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False

        stack = [(root, targetSum)]

        while stack:
            node, cur = stack.pop()

            if not node.left and not node.right:
                if cur == node.val:
                    return True

            if node.right:
                stack.append((node.right, cur - node.val))

            if node.left:
                stack.append((node.left, cur - node.val))

        return False