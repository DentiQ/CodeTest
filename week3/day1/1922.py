import sys
import heapq


def prim(start):
    hq = []
    visit[start] = 1
    result = 0
    for i in graph[start]:
        heapq.heappush(hq, i)

    while hq:
        cost, point = heapq.heappop(hq)
        if not visit[point]:
            visit[point] = 1
            result += cost
            for j in graph[point]:
                heapq.heappush(hq, j)
            if sum(visit) == n:
                return result


input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for i in range(n+1)]
visit = [0] * (n+1)

for i in range(m):
    s, d, c = map(int, input().split())
    graph[s].append([c, d])
    graph[d].append([c, s])

print(prim(1))
