n = int(input())

for i in range(n):
    try:
        stack = []
        string = input()
        for j in string:
            if j == '(':
                stack.append('(')
            elif j == ')':
                if stack:
                    stack.pop()
                else:
                    print("NO")
                    raise NotImplementedError
    except NotImplementedError:
        continue

    if '(' in stack:
        print("NO")
    elif not stack:
        print("YES")
