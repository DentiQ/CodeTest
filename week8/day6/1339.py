N = int(input())

words = [input() for _ in range(N)]

word_dict = {}

ans = 0

for word in words:
    word_len = len(word) - 1
    for letter in word:
        if letter in word_dict:
            word_dict[letter] += 10 ** word_len
        else:
            word_dict[letter] = 10 ** word_len
        word_len -= 1

word_dict = sorted(word_dict.items(), reverse=True, key=lambda item:item[1])

index = 9

for letter, score in word_dict:
    ans += score * index
    index -= 1

print(ans)



