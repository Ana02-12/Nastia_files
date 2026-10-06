from typing import *
class Solution: #[1, 2, 3, 3, 3, 4, 6, 8]
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        l = 0
        for r in range(1, len(nums)):
            if nums[r] != nums[l]:
                l += 1
                nums[l] = nums[r]
        return l + 1
lst = [1, 2, 3, 3, 3, 4, 6, 8]
print(lst[:Solution().removeDuplicates(lst)])


