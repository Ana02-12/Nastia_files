class Solution:
#путь от конца к началу ...........................................................
    def romanToInt(self, s: str) -> int:
        div = {'M': 1000,
               'CM': 900, 'D': 500, 'CD': 400, 'C': 100,
               'XC': 90, 'L': 50, 'XL': 40, 'X': 10,
               'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
        res = 0
        pred = 0
        for ch in reversed(s):
            val = div[ch]
            if val > pred:
                res += val
                pred = val
            else:
                res -= val
        return res
# print(Solution().romanToInt('IV'))
#от начала к концу ...............................................................
    def romanToInt2(self, s: str) -> int:
        div = {
                    'I': 1,
                    'V': 5,
                    'X': 10,
                    'L': 50,
                    'C': 100,
                    'D': 500,
                    'M': 1000
                }
        res = 0
        last = div[s[-1]]
        for a, b in zip(s, s[1:]):
            val_a = div[a]
            val_b = div[b]
            if val_a >= val_b:
                res += val_a
            else:
                res -= val_a
        res += last
        return res
print(Solution().romanToInt2('VI'))