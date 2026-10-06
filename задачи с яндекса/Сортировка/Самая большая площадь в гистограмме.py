def main():
    n = int(input())
    height = list(map(int, input().split()))

    stack = []
    ans = 0

    for i in range(n + 1):
        cur = height[i] if i < n else 0

        while stack and height[stack[-1]] > cur:
            height = height[stack.pop()]

            if stack:
                width = i - stack[-1] - 1
            else:
                width = i

            ans = max(ans, height * width)

        stack.append(i)

    print(ans)


if __name__ == '__main__':
    main()