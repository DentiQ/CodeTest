from sys import stdin
from collections import deque

input = stdin.readline

N, M, V = map(int, input().split())

graph = {}

for i in range(1, N+1):
    graph[i] = []

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(v):
    visited = set()
    stack = [v]

    while stack:
        nv = stack.pop()
        if nv not in visited:
            res.append(nv)
            temp = graph[nv]
            temp.sort(reverse=True)
            for i in temp:
                stack.append(i)
            visited.add(nv)


def bfs(v):
    visited = set()
    queue = deque()
    queue.append(v)

    while queue:
        nv = queue.popleft()
        if nv not in visited:
            res.append(nv)
            temp = graph[nv]
            temp.sort()
            for i in graph[nv]:
                queue.append(i)
            visited.add(nv)


res = []
dfs(V)
print(*res)

res = []
bfs(V)
print(*res)
