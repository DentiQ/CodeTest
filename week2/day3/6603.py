from itertools import combinations

while True:
    s = list(map(int, input().split()))
    if s[0] == 0:
        break
    else:
        s.pop(0)
        combi = list(combinations(s, 6))
        for num in combi:
            print(*num)
        print()

