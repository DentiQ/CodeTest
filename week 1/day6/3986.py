n = int(input())

ans = 0

word_list = list(input() for _ in range(n))

for word in word_list:
    stack = []
    for a in word:
        if (not stack) or (stack[-1] != a):
            stack.append(a)
        else:
            stack.pop()
    if not stack:
        ans += 1

print(ans)
