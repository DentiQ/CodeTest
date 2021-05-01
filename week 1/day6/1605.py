n = int(input())
s = input()
mydict = {}

for i in range(len(s)+1):
    for j in range(len(s)+1):
        try:
            mydict[s[i:j]] += 1
        except:
            mydict[s[i:j]] = 1
del mydict['']

max = 0

for key, val in mydict.items():
    if val > 1:
        if len(key) > max:
            max = len(key)

print(max)
