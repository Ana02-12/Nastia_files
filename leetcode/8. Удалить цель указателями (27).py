def removeElement(nums, val):
    l = 0
    for r in range(len(nums)):
        if nums[r] != val:
            nums[l] = nums[r]
            l += 1

    return [l, nums]
print(removeElement([1, 2, 2, 2, 3, 4], 2))