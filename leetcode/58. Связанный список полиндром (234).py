class Solution:
    def isPalindrome(self, head) -> bool:
        # 1. Находим середину списка
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Разворачиваем вторую половину
        prev = None

        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        # 3. Сравниваем первую и развернутую вторую половины
        left = head
        right = prev

        while right:
            if left.val != right.val:
                return False

            left = left.next
            right = right.next

        return True