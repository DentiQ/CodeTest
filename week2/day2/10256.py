from itertools import product

T = int(input())

for i in range(T):
    n, m = map(int, input().split())

    dna = input()
    marker = input()

    markers = []

    marker_index = list(product(list(range(m)), repeat=2))
    print(marker_index)
    for i in marker_index:
        markers.append(marker[:i[0]] + marker[i[0]:i[1]] + marker[i[1]:])

    print(markers)
