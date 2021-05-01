var = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
op1 = "*/"
op2 = "+-"
ans = ""
stack = []

state = input()

for i in state:
    if i in var:
        ans += i
    elif i == '(':
        stack.append(i)
    elif i in op1:
        while stack and stack[-1] in op1:
            ans += stack.pop()
        stack.append(i)
    elif i in op2:
        while stack and stack[-1] != "(":
            ans += stack.pop()
        stack.append(i)
    elif i == ")":
        while stack and stack[-1] != "(":
            ans += stack.pop()
        stack.pop()


while stack:
    ans += stack.pop()

print(ans)



