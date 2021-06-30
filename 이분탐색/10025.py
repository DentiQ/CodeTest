"""
https://www.acmicpc.net/problem/10025
게으른 백곰

문제
더운 여름날 동물원의 백곰 앨버트는 너무 더워서 꼼짝도 하기 싫다.
다행히도 사육사들이 앨버트의 더위를 식히기 위해 얼음이 담긴 양동이들을 가져다 주었다. 앨버트가 가장 적은 거리만 움직이고도 최대한 많은 얼음으로 더위를 식힐 수 있도록 도와주자.
우리 안은 1차원 배열로 생각하며, 총 N(1 ≤ N ≤ 100000)개의 얼음 양동이들이 xi(0 ≤ xi ≤ 1,000,000)좌표마다 놓여 있고 각 양동이 안에는 gi(1 ≤ gi ≤ 10,000)씩의 얼음이 들어있다.
일단 앨버트가 자리를 잡으면 그로부터 좌우로 K(1 ≤ K ≤ 2,000,000) 만큼 떨어진 양동이까지 닿을 수 있다. 앨버트는 양동이가 놓여 있는 자리에도 자리잡을 수 있다. 모든 얼음 양동이의 위치는 다르다.
앨버트가 최적의 자리를 골랐을 때 얼음의 합을 구하시오. 즉, 얼음들의 합의 최댓값을 구해야 한다.

입력
첫 줄에 정수 N과 K가 들어온다. 둘째 줄부터 N째 줄까지, 공백을 사이에 두고 각 양동이의 얼음의 양을 나타내는 gi와 양동이의 좌표를 나타내는 xi가 주어진다.

출력
앨버트가 택한 최적 위치로부터 K만큼 떨어진 거리 내에 있는 얼음들의 합(최댓값)을 출력한다.
"""
from sys import stdin
from collections import deque

input = stdin.readline

N, K = map(int, input().split())

ice = [0 for _ in range(1000001)]

left, right = 1000002, 0
q = deque()

for _ in range(N):
    g, x = map(int, input().split())
    ice[x] = g
    left = min(left, x)
    right = max(right, x)

max_ice, temp = 0, 0

for t in range(left, right+1):
    if len(q) < 2*K + 1:
        q.append(ice[t])
        temp += ice[t]
        max_ice = temp
    else:
        temp -= q.popleft()
        q.append(ice[t])
        temp += ice[t]
        max_ice = max(max_ice, temp)

print(max_ice)
