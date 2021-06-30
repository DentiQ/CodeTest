"""
https://www.acmicpc.net/problem/2865
나는 위대한 슈퍼스타K

문제
상근이는 한국 최고의 가수를 뽑는 "나는 위대한 슈퍼스타K"의 감독이다. 상근이는 다음과 같이 참가자를 선발하려고 한다.
"나는 위대한 슈퍼스타K"의 예선에는 N명이 참가했고, 서로 다른 M개 장르에 대한 오디션을 보았다. 심사위원은 모든 참가자의 각 장르에 대한 능력을 점수로 매겼다. 이 점수는 실수로 나타낸다.
본선에는 총 K명이 나갈 수 있다. 각 참가자는 본선에서 단 하나의 장르만 부를 수 있고, 이 장르는 상근이가 정해준다. 한 사람이 여러 장르를 부를 수는 없지만, 여러 사람이 같은 장르를 부를 수는 있다.
모든 참가자의 각 장르에 대한 능력이 주어진다. 이때, 능력의 합이 최대가 되도록 참가자와 장르를 선택하는 프로그램을 작성하시오.

입력
첫째 줄에 N, M, K가 주어진다. (1 ≤ M ≤ 100, 1 ≤ K ≤ N ≤ 100)
다음 M개의 줄은 각 장르에 대한 참가자의 능력이 주어진다. 이 줄에는 N개의 (i, s)쌍이 주어진다. 여기서 i는 참가자의 번호, s는 그 참가자의 장르에 대한 능력이다. 이 쌍은 능력이 감소하는 순서대로 주어진다. 참가자의 번호는 1부터 N까지 이다.
각 줄에 모든 학생은 한 번씩 등장한다.

출력
첫째 줄에 본선 참가자의 능력의 합을 소수점 첫째자리까지 반올림해 출력한다.
"""
from sys import stdin

input = stdin.readline

n, m, k = map(int, input().split())
singers = [0.0] * n

for i in range(m):
    arr_in = input().split()

    for j in range(n):
        singer, skill = int(arr_in[2 * j]) - 1, float(arr_in[2 * j + 1])
        singers[singer] = max(singers[singer], skill)

print(round(sum(sorted(singers, reverse=True)[:k]), 1))