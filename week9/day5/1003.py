T = int(input())

fibo0 = [1, 0]
fibo1 = [0, 1]

for i in range(2, 41):
    fibo0.append(fibo0[i - 1] + fibo0[i - 2])
    fibo1.append(fibo1[i - 1] + fibo1[i - 2])

for _ in range(T):
    N = int(input())
    print(fibo0[N], fibo1[N])
