doc = input()
word = input()

index = 0
doc_len = len(doc)
word_len = len(word)

ans = 0

while True:
    if index > doc_len - word_len:
        break

    if doc[index:word_len+index] == word:
        ans += 1
        index += word_len
    else:
        index += 1

print(ans)
