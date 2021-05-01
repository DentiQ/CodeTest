from sys import stdin

n = int(input())
S = set()

for i in range(n):
    temp = stdin.readline().split()
    if len(temp) == 1:
        if temp[0] == "all":
            S = set(i for i in range(1, 21))
        else:
            S = set()
    else:
        op, num = temp[0], int(temp[1])
        if op == "add":
            S.add(num)
        elif op == "remove":
            S.discard(num)
        elif op == "check":
            print(int(num in S))
        elif op == "toggle":
            if num in S:
                S.discard(num)
            else:
                S.add(num)
