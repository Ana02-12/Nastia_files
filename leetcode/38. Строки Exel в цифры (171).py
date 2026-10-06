def titleToNumber(columnTitle):
    ans = 0
    power = 0
    for ch in columnTitle[::-1]:
        cur_val = (ord(ch) - ord('A') + 1)
        ans += cur_val * 26**power
        power += 1
    return ans
#второй способ -=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-==-
def titleToNumber(columnTitle):
    result = 0

    for char in columnTitle:
        result = result * 26 + (ord(char) - ord('A') + 1)

    return result
