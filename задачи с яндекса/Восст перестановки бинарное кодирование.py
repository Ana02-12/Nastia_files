n = int(input())

# ans[position] = номер детали
ans = [0] * n

bits = (n - 1).bit_length()

for bit in range(bits):
    # Детали, у которых этот бит равен 1
    parts = []

    for part in range(1, n + 1):
        if (part - 1) & (1 << bit):
            parts.append(part)

    # Запрашиваем позиции этих деталей
    print("CHECK", *parts, flush=True)

    positions = list(map(int, input().split()))

    # На этих позициях находятся детали,
    # у которых текущий бит равен 1
    for pos in positions:
        ans[pos - 1] |= (1 << bit)

print("RESULT", *ans, flush=True)