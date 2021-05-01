import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

tree = [[] for _ in range(n+1)]
graph = [[] for _ in range(n + 1)]

for i in range(1, n+1):
    node_list = list(map(int, input().split()))
    for j in range(1, len(node_list)//2):
        tree[node_list[0]].append([node_list[2*j-1], node_list[2*j]])
    start = node_list[0]
    k = 1
    while 1:
        to = node_list[k]
        if to == -1:
            break
        cost = node_list[k + 1]
        graph[start].append((to, cost))
        k += 2

print(tree)
print(graph)


def bfs(root):
    q = deque()
    q.append((root, 0))
    dist = [-1] * (n+1)
    while q:
        v, cost = q.popleft()
        for to_v, n_cost in tree[v]:
            if dist[to_v] == -1:
                dist[to_v] = cost + n_cost
                q.append((to_v, dist[to_v]))
    far = max(dist)
    index = dist.index(far)
    return index, far


x_to_y = bfs(1)[0]
ans = bfs(x_to_y)[1]

print(ans)


