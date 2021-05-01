from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    visited = [False] * 10000

    visited[a] = True

    queue = deque()
    queue.append([a, ""])

    while queue:
        num, ops = queue.popleft()

        if num == b:
            print(*ops, sep="")
            break

        if not visited[(num * 2) % 10000]:
            visited[num * 2 % 10000] = True
            queue.append([num * 2 % 10000, ops + "D"])

        if not visited[(num - 1) % 10000]:
            visited[(num - 1) % 10000] = True
            queue.append([(num - 1) % 10000, ops + "S"])

        if not visited[num % 1000 * 10 + num // 1000]:
            visited[num % 1000 * 10 + num // 1000] = True
            queue.append([num % 1000 * 10 + num // 1000, ops + "L"])

        if not visited[num % 10 * 1000 + num // 10]:
            visited[num % 10 * 1000 + num // 10] = True
            queue.append([num % 10 * 1000 + num // 10, ops + "R"])