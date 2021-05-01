string = input()

stack = []

temp = 0
ans = 0

def popallint():
    temp2 = 0
    while True:
        if stack[-1] == int:
            temp2 += stack.pop(-1)
        else:
            return temp2

for i in range(len(string)):
    if string[i] == '(':
        stack.append('(')

    elif string[i] == '[':
        stack.append('[')

    elif string[i] == ')':
        if not stack:
            print(0)
            break
        elif stack[-1] == '(':
            temp += 2
        elif stack[-1] == int:
            temp += popallint()
            temp *= 3
            print(0)
            break

    elif i == ']':
        if not stack:
            print(0)
            break
        elif stack[-1] == '[':

            print(temp)
            stack.pop(-1)
        else:
            print(0)
            break

print(ans)