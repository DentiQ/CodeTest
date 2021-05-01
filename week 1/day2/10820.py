upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
num = "0123456789"

for i in range(100):
    try:
        word = input()
        ans = [0,0,0,0]
        for i in word:
            if i in lower: ans [0] = ans[0]+1
            elif i in upper: ans[1] = ans[1]+1
            elif i in num: ans[2] = ans[2]+1
            elif i == ' ': ans[3] = ans[3]+1

        print(str(ans[0]) + ' ' + str(ans[1]) + ' ' + str(ans[2]) + ' ' + str(ans[3]))
    except:
        break

