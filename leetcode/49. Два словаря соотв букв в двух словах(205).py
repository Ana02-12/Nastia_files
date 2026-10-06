def isIsomorphic(s, t):
    s_to_t = {}
    t_to_s = {}
    for s_char, t_char in zip(s, t):
        #если s есть в своем словаре
        if s_char in s_to_t:
            #проверим его значение
            if s_to_t[s_char] != t_char:
                return False
        #если s нет в его словаре
        else:
            s_to_t[s_char] = t_char
        #если t есть в своем словаре
        if t_char in t_to_s:
            #проверим его значение
            if t_to_s[t_char] != s_char:
                return False
        #если t нет в его словаре
        else:
            t_to_s[t_char] = s_char
    return True