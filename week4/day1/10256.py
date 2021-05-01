import sys

input = sys.stdin.readline

t = int(input())


def convert(string):
    string = string.replace('A', '1')
    string = string.replace('G', '2')
    string = string.replace('T', '3')
    string = string.replace('C', '4')

    return string


def get_hash(string):
    index = m-1
    hash = 0
    for num in string:
        hash += int(num) * (2 ** index)
        index -= 1
    return hash % 1000000001


for _ in range(t):
    n, m = map(int, input().split())

    dna = input().replace('\n', '')
    marker = input().replace('\n', '')

    markers = []

    for i in range(m):
        for j in range(i+1, m):
            tmp = marker[:i] + ''.join(reversed(marker[i:j+1])) + marker[j+1:m]
            markers.append(tmp)

    ans = 0

    dna = convert(dna)

    for marker in markers:
        marker = convert(marker)
        hash = get_hash(marker)
        print(marker)
        text_index = 0
        text_hash = (get_hash(dna[text_index:text_index + m])) % 1000000001
        while text_index <= n-m:
            print('{} {} {}'.format(dna[text_index:text_index+m],text_hash, hash))
            if text_hash == hash:
                if dna[text_index:text_index+m] == marker:
                    ans += 1
            text_hash = (2 * (text_hash - (2**(m-1))*int(dna[text_index]))) + (int(dna[text_index+m-1]))
            text_hash %= 1000000001
            text_index += 1

        print('-----')

    print(ans)
