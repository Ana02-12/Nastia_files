def canConstruct(ransomNote, magazine):
    cnt = {}
    for m in magazine:
        cur = cnt.get(m, 0)
        cnt[m] = cur + 1

    for r in ransomNote:
        if r not in cnt:
            return False
        if cnt[r] > 0:
            cnt[r] -= 1
        else:
            return False
    return True

