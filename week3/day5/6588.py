import sys

is_prime = [False, False] + [True for i in range(999999)]

for i in range(2, 1000001):
    if is_prime[i]:
        for j in range(i+i, 1000001, i):
            is_prime[j] = False

while True:
    num = int(sys.stdin.readline())
    flag = True
    if num == 0:
        break
    for i in range(2, 1000000):
        if is_prime[i] and is_prime[num-i]:
            print("{} = {} + {}".format(num, i, num-i))
            flag = False
            break
    if flag:
        print("Goldbach's conjecture is wrong.")


