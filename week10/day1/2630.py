from sys import stdin

input = stdin.readline

N = int(input())

paper = [list(map(int, input().split())) for _ in range(N)]

white, blue = 0, 0


def color(x, y, size):
    global white, blue

    print(x, y, size)

    if size == 1:
        if paper[x][y] == 0:
            white += 1
        else:
            blue += 1

    else:
        flag = False
        temp = paper[x][y]
        for i in range(x, x+size):
            if flag:
                break
            for j in range(y, y+size):
                if temp != paper[i][j]:
                    flag = True
                    break
        if not flag:
            if temp == 0:
                white += 1
            elif temp == 1:
                blue += 1
        else:
            dx = [0, 0, size//2, size//2]
            dy = [0, size//2, 0, size//2]

            for i in range(4):
                color(x + dx[i], y + dy[i], size//2)


color(0, 0, N)

print(white)
print(blue)
