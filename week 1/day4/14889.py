import itertools

n = int(input())
stat = []
team = list(range(0, n))

combinations = list(itertools.combinations(team, n // 2))

for i in range(n):
    temp_array = []
    temp_input = input().split()
    for j in range(n):
        temp_array.append(int(temp_input[j]))
    stat.append(temp_array)

for i in range(len(combinations) // 2):
    team1 = 0
    team2 = 0
    permutation1 = list(itertools.permutations(combinations[i], 2))
    for j in permutation1:
        team1 += stat[j[0]][j[1]]

    permutation2 = list(itertools.permutations(combinations[-i - 1], 2))
    for j in permutation2:
        team2 += stat[j[0]][j[1]]

    if i == 0:
        ans = abs(team1 - team2)
    else:
        if ans > abs(team1 - team2):
            ans = abs(team1 - team2)
print(ans)
