def isPowerOfTwo(n):
    if n <= 0: return False
    min_one = n - 1
    without_one = n & min_one
    return without_one == 0

print(isPowerOfTwo(2))


