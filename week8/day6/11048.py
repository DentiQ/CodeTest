from sys import stdin

input = stdin.readline

N, M = map(int, input().split())

maze = [[0] + list(map(int, input().split())) for _ in range(N)]

maze.insert(0, [0 for _ in range(M+1)])

for i in range(1, N+1):
    for j in range(1, M+1):
        maze[i][j] += max(maze[i-1][j], maze[i][j-1], maze[i-1][j-1])

print(maze[N][M])