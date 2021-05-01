n = int(input())

buildings = []
time = []

for i in range(n):
    buildings.append(list(map(int, input().split())))

for i in range(n):
    if len(buildings[i]) > 2:
        for j in range(1, len(buildings[i])):
            buildings[i][j] -= 1

for i in range(n):
    q = []
    temp = set()

    if len(buildings[i]) == 2:
        print(buildings[i][0])
    else:
        for j in buildings[i][1:-1]:
            q.append(j)
        while q:
            build = q.pop()
            temp.add(build)
            if len(buildings[build]) != 2:
                for k in buildings[build][1:-1]:
                    if k not in temp:
                        q.append(k)

        ans = buildings[i][0]

        for l in temp:
            ans += buildings[l][0]

        print(ans)











