import copy
a = []

for i in range(9):
    a.append(int(input()))


for i in range(9):
    for j in range(9):
        if i != j:
            temp = sum(a) - a[i] - a[j]
            if temp == 100:
                b = copy.deepcopy(a)
                b.sort()
                b.remove(a[i])
                b.remove(a[j])
                for k in b:
                    print(k)
                exit()
