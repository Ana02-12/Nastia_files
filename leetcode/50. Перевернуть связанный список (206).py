class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def reverseList(head):
    #узел на, которого будут указывать следующие
    prev = None
    #текущий узел
    cur = head

    while cur:
        #сохраним след узел для обработки
        nxt = cur.next
        #текущий указывает на начало нового списка
        cur.next = prev
        #текущий стал концом нового списка
        prev = cur
        #следующий стал текущим
        cur = nxt

    return prev



