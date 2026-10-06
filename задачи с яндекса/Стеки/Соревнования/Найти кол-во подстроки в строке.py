def main():
    s = input()
    t = input()

    #соберем патерн
    pattern = {}
    for ch in t:
        pattern[ch] = pattern.get(ch, 0) + 1

    #текущие символы
    cur = {}
    l = 0
    cnt = 0

    for r in range(len(s)):
        ch = s[r]
        cur[ch] = cur.get(ch, 0) + 1

        #двигаем левый, если патерн нарушен
        while cur[ch] > pattern.get(ch, 0):
            ch_l = s[l] #левый
            cur[ch_l] -= 1 #уберем из текущих
            l += 1 #пододвинем
        cnt += r - l + 1
    print(cnt)

#второй способ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def main():
    s = input()
    t = input()

    #соберем патерн
    int_t = {}
    for ch in t:
        int_t[ch] = int_t.get(ch, 0) + 1

    #текущие символы
    now = {}
    #r будет невключительно
    l = r = 0
    ans = 0

    while r < len(s):
        #до тех пор, пока не вышли за пределы строки
        #и пока текущее кол-во меньше патерна
        #мы добавим символ только в этом случае
        while r < len(s) and \
                now.get(s[r], 0) < int_t.get(s[r], 0):
            now[s[r]] = now.get(s[r], 0) + 1
            r += 1
            ans += r - l #длинна невключительно
        if l < r:
            now[s[l]] -= 1
        l += 1
        #если левый перешагнул правый
        r = max(l, r)

    print(ans)

