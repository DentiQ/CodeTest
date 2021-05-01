def buttonPossible(num, broken):
    num = str(num)
    for i in num:
        if i in broken:
            return False
    return True


ch = int(input())
n = int(input())
if n != 0:
    broken = input().split()

ans = abs(100 - ch)

for i in range(1000001):
    if buttonPossible(i, broken):
        ans = min(ans, abs(i - ch) + len(str(i)))

print(ans)
