import sys
from itertools import product

input = sys.stdin.readline

n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    while True:
        i = 1
        flag = False
        prod = product(list(range(4)), repeat=i)
        ans = tuple()
        for case in prod:
            temp = a
            for letter in case:
                if letter == 0:
                    temp = (2*a) % 10000
                elif letter == 1:
                    if temp == 0:
                        temp = 9999
                    else:
                        temp -= 1
                elif letter == 2:
                    temp2 = str(temp)
                    while len(temp2) == 4:
                        temp2 = "0" + temp2
                    temp2 = list(temp2)
                    temp2[0], temp2[1], temp2[2], temp2[3] = temp2[1], temp2[2], temp2[4], temp2[0]
                    temp2 = ''.join(temp2)
                    temp = int(temp2)
                elif letter == 3:
                    temp2 = str(temp)
                    while len(temp2) == 4:
                        temp2 = "0" + temp2
                    temp2 = list(temp2)
                    temp2[0], temp2[1], temp2[2], temp2[3] = temp2[3], temp2[0], temp2[1], temp2[2]
                    temp2 = ''.join(temp2)
                    temp = int(temp2)
                if temp == b:
                    ans = case
                    flag = True
                    break
            if flag:
                break
        if flag:
            for letter in ans:
                if i == 0:
                    print("D", end="")
                elif i == 1:
                    print("S", end="")
                elif i == 2:
                    print("L", end="")
                elif i == 3:
                    print("R", end="")
            print()
        else:
            i += 1