def main():
    s = input()

    pat = {'(': ')',
           '[': ']',
           '{': '}'}

    stack = []
    for ch in s:
        if ch in pat:
            stack.append(ch)

        else:
            if not stack:
                return False
            
            last = stack.pop()
            if pat[last] != ch:
                return False
    return not stack


