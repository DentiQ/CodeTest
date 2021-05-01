from collections import deque
import sys

input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[0]*(n+1) for i in range(n+1)]

for i in range(m):
    start, dest = map(int, input().split())
    graph[start][dest] = graph[dest][start] = 1


def DFS(graph, start):
    visited = [start]
    stack = [start]
    while stack:
        n = stack.pop()
        if (graph[n][i] == 1 or graph[i][n] == 1) and (i not in visited):
            visited.append(i)
            stack.append(i)
    return print(*visited)


def BFS(graph, start):
    visited = [start]
    queue = deque([start])

    while queue:
        n = queue.popleft()
        for i in range(len(graph[start])):
            if graph[n][i] == 1 and (i not in visited):
                visited.append(i)
                queue.append(i)
    return print(*visited)

DFS(graph, v)
BFS(graph, v)