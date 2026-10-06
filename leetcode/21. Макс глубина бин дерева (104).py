#рекурсия -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def mxDepth(root):
    if not root:
        return 0
    lt = mxDepth(root.left)
    rt = mxDepth(root.right)
    return max(lt, rt) + 1
#итеративный -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0

        stack = [(root, 1)]
        ans = 0

        while stack:
            node, depth = stack.pop()
            if not node.left and not node.right:
                ans = max(ans, depth)
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))

        return ans

