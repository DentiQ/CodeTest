from itertools import product

N, M = map(int, input().split())

arr = sorted(list(set(map(int, input().split()))))

ans = list(product(arr, repeat=M))

for i in ans:
    flag = True
    temp = -1
    for num in i:
        if temp > num:
            flag = False
            break
        else:
            temp = num
    if flag:
        print(*i)