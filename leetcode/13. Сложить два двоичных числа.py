class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        res = []

        idxA, idxB = len(a) - 1, len(b) - 1

        while idxA >= 0 or idxB >= 0 or carry == 1:
            #если не дошли до конца A
            if idxA >= 0:
                carry += int(a[idxA])
                idxA -= 1
            #если не дошли до конца В
            if idxB >= 0:
                carry += int(b[idxB])
                idxB -= 1

            res.append(str(carry % 2))
            carry = carry // 2

        return "".join(res[::-1])
print(Solution().addBinary( '101', '11'))
