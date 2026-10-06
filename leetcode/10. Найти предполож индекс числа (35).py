def searchInsert(nums, target: int):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            right = mid - 1
        elif target > nums[mid]:
            left = mid + 1

    return left
lsts = [1, 2, 3, 4, 5, 6, 7, 9]
print(searchInsert(lsts, 8))