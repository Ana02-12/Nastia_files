#через коллекции -=-=-=-=-=-=-=-=-=-=-=-==-=-
from collections import Counter
def isAnagram(s, t):
    #хранит словари с кол-вом встреч
    #каждой из букв
    return Counter(s) == Counter(t)

#вручную через словари -=-=-=-=-=-=-=-=-=-=-=
def isAnagram(s, t):
    #разная длинна
    if len(s) != len(t):
        return False

    #пройдем по первому слову
    #задаем паттерн
    let_cnt = {}
    for ch in s:
        #возьмем его старое количество
        old = let_cnt.get(ch, 0)
        #прибавим +1
        let_cnt[ch] = old + 1

    #проверим второе слово
    for ch in t:
        #если его нет в заданном паттерне
        if ch not in let_cnt:
            return False
        #если он есть вычтем его
        let_cnt[ch] -= 1
        #если букв было слишком много
        if let_cnt[ch] < 0:
            return False
    return True





