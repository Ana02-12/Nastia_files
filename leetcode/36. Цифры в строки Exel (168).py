#через unicode -=-=-==-=-=-=-=-==-=-=-=-==--=-=-=-=-=-=-=-=
def convertToTitle(columnNumber) -> str:
    res = ""
    while columnNumber > 0:
        offs = (columnNumber - 1) % 26
        res += chr((ord("A") + offs))
        columnNumber = (columnNumber - 1) // 26
    return res[::-1]

#-=-=-=-=-=-=--=-=-==-=-=-=-=-==-=-=-=-==--=-=-=-=-=-=-=-=-=
def to_col(n):
    col = ''
    while n > 0:
        n -= 1 # На каждом разряде (на каждой итерации) теряем 1
        col = chr(ord('A') + n % 26) + col
        n //= 26
    return col
#без -1 -=-=-==-=-=-=-=-==-=-=-=-==--=-=-=-=-=-=-=-=-=-=-=-=
from string import ascii_uppercase

s = ascii_uppercase
res = []
n = 100

while n:
    rem = n % 26

    if rem == 0:
        res.append('Z')
        n = n // 26 - 1
    else:
        res.append(s[rem - 1])
        n //= 26

print("".join(reversed(res)))
