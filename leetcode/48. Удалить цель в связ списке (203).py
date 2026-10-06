class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def removeElements(head, val):
    #фиктивный узел, чтобы всегда смотреть на next
    dummy = ListNode(0)
    #прикрепим его к списку
    dummy.next = head
    #поставим двигающийся указатель
    cur = dummy
    #пока существует следующий узел
    while cur.next:
        #если нашли таргет
        if cur.next.val == val:
            #переназначим
            cur.next = cur.next.next
        #сдвинем указатель
        cur = cur.next
    return dummy.next

