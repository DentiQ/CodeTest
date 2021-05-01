string = input()
ans = 0
temp = 0
for i in range(len(string)):
    if string[i] == '(':
        if string[i+1] == '(':
            temp += 1
        else:
            ans += temp

    elif string[i] == ')':
        if string[i-1] == '(':
            continue
        else:
            ans += 1
            temp -= 1

print(ans)





