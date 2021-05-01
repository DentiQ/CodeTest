import sys

input = sys.stdin.readline

string = input().strip()
bomb = input().strip()

stack = []

for char in string:
    stack.append(char)
    if len(stack) >= len(bomb):
        while True:
            if len(stack) >= len(bomb):
                flag = True
                for i in range(len(bomb)):
                    if stack[i + len(stack) - len(bomb)] == bomb[i]:
                        continue
                    else:
                        flag = False
                        break
                if flag:
                    for _ in range(len(bomb)):
                        stack.pop()
                else:
                    break
            else:
                break

if stack:
    print(''.join(stack))
else:
    print('FRULA')

