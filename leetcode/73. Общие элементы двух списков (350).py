def f(nums1, nums2):
    cnt = {}
    for n in nums1:
        cur = cnt.get(n, 0)
        cnt[n] = cur + 1

    res = []
    for val in nums2:
        if val in cnt and cnt[val] > 0:
            res.append(val)
            cnt[val] -= 1
    return res

print(f(['1', '1', '1', '2'], ['2', '2', '1']))

