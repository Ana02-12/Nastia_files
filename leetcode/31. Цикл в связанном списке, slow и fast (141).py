def hasCycle(head):
    sl, fs = head, head
    while fs and fs.next:
        sl = sl.next
        fs = fs.next.next
        if sl == fs:
            return True
    return False

