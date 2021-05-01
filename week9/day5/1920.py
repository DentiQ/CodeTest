import sys

input = sys.stdin.readline

n = int(input())
An = set(map(int, input().split()))

m = int(input())
Am = list(map(int, input().split()))

for num in Am:
    if num in An:
        sys.stdout.write('1\n')
    else:
        sys.stdout.write('0\n')