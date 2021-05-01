import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())

city_map = []

for _ in range(n):
    city_map.append(list(map(int, input().split())))

houses = []
chickens = []

for x in range(n):
    for y in range(n):
        if city_map[x][y] == 1:
            houses.append([x, y])
        elif city_map[x][y] == 2:
            chickens.append([x, y])


def distance(house, chicken):
    return abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])


chicken_queue = list(combinations(chickens, m))

ans = float('inf')

for queue in chicken_queue:
    city_dist = 0
    for house in houses:
        dist = float('inf')
        for chicken in queue:
            dist = min(dist, distance(house, chicken))
        city_dist += dist
    ans = min(ans, city_dist)

print(ans)