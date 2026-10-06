class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#рекурсия -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def sortedArrayToBST(nums):
    l = 0
    r = len(nums) - 1
    def build(l, r):
        if l > r:
            return None

        mid = (l + r) // 2

        root = TreeNode(nums[mid])
        root.left = build(l, mid - 1)
        root.right = build(mid + 1, r)

        return root

    return build(l, r)
#стек -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        if not nums:
            return None

        # Создаем фиктивный корень, чтобы унифицировать логику для всех узлов
        dummy = TreeNode(0)

        # Стек хранит кортежи: (родительский_узел, левая_граница, правая_граница, является_ли_левым)
        stack = [(dummy, 0, len(nums) - 1, True)]

        while stack:
            parent, l, r, is_left = stack.pop()

            if l > r:
                continue

            mid = (l + r) // 2
            node = TreeNode(nums[mid])

            # Корректно связываем родителя с текущим созданным узлом
            if is_left:
                parent.left = node
            else:
                parent.right = node

            # Добавляем в стек задачи на построение детей текущего узла
            # Порядок добавления (левый/правый) теперь не нарушает связи родитель-ребенок
            stack.append((node, l, mid - 1, True))
            stack.append((node, mid + 1, r, False))

        return dummy.left