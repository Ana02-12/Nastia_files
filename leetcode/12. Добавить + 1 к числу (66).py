def f(digits):
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] != 9:
            digits[i] += 1
            return digits
        else:
            digits[i] = 0
            if i == 0:
                return [1] + digits
print(f([9, 9, 9]))