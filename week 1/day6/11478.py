s = input()
ans = {}
for i in range(len(s)+1):
    for j in range(len(s)+1):
        ans.add(s[i:j])

print(len(ans)-1)
