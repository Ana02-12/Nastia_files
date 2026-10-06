def isValid( s: str) -> bool:
    pairs = {
        '[': ']',
        '(': ')',
        '{': '}'
    }
    stack = []
    for ch in s:
        #если открывающая
        if ch in pairs:
            stack.append(ch)
        #если закрывающая
        else:
            #Нет открывающей скобки для закрытия
            if not stack: return False
            #Извлекаем последнюю открытую скобку
            last = stack.pop(-1)
            #Для неё ожидалась другая закрывающая скобка
            if pairs[last] != ch: return False
    return not stack
print(isValid('()[[]'))