from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            val = nums[i]
            coplement = target - val
            if coplement in hash_map:
                return [i, hash_map[coplement]]
            else:
                hash_map[val] = i
        else:
            return []
lst = [2, 7, 11, 15]
target = 9
print(Solution().twoSum(lst, target))