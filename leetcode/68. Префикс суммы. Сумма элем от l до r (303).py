class NumArray:
    #создать префиксные суммы
    def __init__(self, nums):
        #мы добавили ноль
        self.pref = [0]
        for i in range(len(nums)):
            cur = self.pref[-1] + nums[i]
            self.pref.append(cur)

    #найти сумму от l до r включительно
    #
    def sumRange(self, left: int, right: int) -> int:
        return self.pref[right + 1] - self.pref[left]
    