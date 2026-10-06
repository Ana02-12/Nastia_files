def f(pattern, s):
    #получим отдельные слова
    words = s.split()
    #проверим длинну
    if len(words) != len(pattern):
        return False

    ch_to_w = {}
    w_to_ch = {}

    for ch, w in zip(pattern, words):
        #первый словарь
        if ch not in ch_to_w:
            ch_to_w[ch] = w
        else:
            if ch_to_w[ch] != w:
                return False

        #второй словарь
        if w not in w_to_ch:
            w_to_ch[w] = ch
        else:
            if w_to_ch[w] != ch:
                return False
    #если всё прошло удачно
    return True



