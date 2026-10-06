class Solution:
    def countBits(self, n: int):
        res = [0]
        for i in range(1, n+1):
            #убрали самую правую единицу
            pred = (i - 1) & i
            #в текущем числе на единицу больше
            cur = res[pred] + 1
            res.append(cur)
        return res

