alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
ans = [-1 for i in range(26)]
word = input()

for i in range(len(word)):
    for j in range(26):
        if word[i] == alphabet[j] and ans[j] == -1:
            ans[j] = i
            break

for i in range(len(ans)):
    print(str(ans[i]) + " ", end='')


