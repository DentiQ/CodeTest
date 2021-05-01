import sys

input = sys.stdin.readline

t = int(input())


def convert(string):
    string = string.replace('A', '1')
    string = string.replace('G', '2')
    string = string.replace('T', '3')
    string = string.replace('C', '4')

    return string


def get_hash(string):
    index = len(string) - 1
    hash = 0
    for num in string:
        hash += (int(num) * (2 ** index)) % 1000000001
        index -= 1
    return hash


for _ in range(t):
    n, m = map(int, input().split())

    dna = input().replace('\n', '')
    marker = input().replace('\n', '')
    marker = convert(marker)

    markers = []
    marker_set = {}

    for i in range(m):
        for j in range(i + 1, m):
            tmp = marker[:i] + ''.join(reversed(marker[i:j + 1])) + marker[j + 1:m]
            markers.append(tmp)

    ans = 0

    dna = convert(dna)

    for marker in markers: # 마커의 해쉬값과 마커를 딕셔너리에 저장 - 해쉬값 - [마커1, 마커2]
        hash = get_hash(marker)
        if hash not in marker_set:
            marker_set[hash] = [marker]
        else:
            marker_set[hash].append(marker)

    dna_hash = get_hash(dna[0:m])

    if n == m:
        if dna_hash in marker_set:
            if dna in marker_set[dna_hash]:
                ans += 1
        print(ans)

    else:
        for index in range(n - m + 1): # 전체 DNA를 선형으로 탐색
            if dna_hash in marker_set:
                if dna[index:index+m] in marker_set[dna_hash]:
                    ans += 1
            if index < n-m: # 다음 해쉬값을 구하는 과정
                dna_hash = (2 * (dna_hash - (int(dna[index]) * (2 ** (m - 1)))) + int(dna[index + m])) % 1000000001

        print(ans)
