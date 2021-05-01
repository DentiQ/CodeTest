N, M = map(int, input().split())

S = list(input())
T = list(input())

idxS = len(S) - 1
idxT = len(T) - 1

train = []

ans = 0

for i in range(N):
    for j in range(M):

        s = S[i:]
        t = T[j:]
        print(s, t)
        while True:
            if not train or train[-1] == 'O':
                if s:
                    if s[0] == 'I':
                        train.append(s.pop(0))
                elif t:
                    if t[0] == 'I':
                        train.append(t.pop(0))
                else:
                    ans = max(ans, len(train)-1)
                    break

            elif train[-1] == 'I':
                if s:
                    if s[0] == 'O':
                        train.append(s.pop(0))
                elif t:
                    if t[0] == 'O':
                        train.append(t.pop(0))
                else:
                    ans = max(ans, len(train))
                    break

print(ans)