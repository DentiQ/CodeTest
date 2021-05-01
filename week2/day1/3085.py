def checkcandy(candy):
    maxcandy = 1

    for i in range(len(candy)):
        temp1 = 1
        temp2 = 1
        for j in range(1, len(candy)):
            if candy[i][j] == candy[i][j - 1]:
                temp1 += 1
            else:
                maxcandy = max(maxcandy, temp1)
                temp1 = 1
            if candy[j][i] == candy[j - 1][i]:
                temp2 += 1
            else:
                maxcandy = max(maxcandy, temp2)
                temp2 = 1
        maxcandy = max(maxcandy, temp1, temp2)
    return maxcandy


n = int(input())
candy = []

ans = 0

for i in range(n):
    candy.append(list(input()))

for i in range(n):
    for j in range(n-1):
        if candy[i][j] != candy[i][j + 1]:
            candy[i][j], candy[i][j + 1] = candy[i][j + 1], candy[i][j]
            ans = max(ans, checkcandy(candy))
            candy[i][j], candy[i][j + 1] = candy[i][j + 1], candy[i][j]

        if candy[j][i] != candy[j + 1][i]:
            candy[j][i], candy[j + 1][i] = candy[j + 1][i], candy[j][i]
            ans = max(ans, checkcandy(candy))
            candy[j][i], candy[j + 1][i] = candy[j + 1][i], candy[j][i]

print(ans)