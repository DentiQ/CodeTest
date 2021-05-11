from sys import stdin

input = stdin.readline

while True:
    mystr = input().rstrip()

    if mystr == ".":
        print("yes")
        break

    arr = []
    ans = True

    for i in mystr:
        if i == "[" or i == "(":
            arr.append(i)

        elif i == "]":
            if not arr or arr[-1] == "(":
                ans = False
                break
            elif arr[-1] == "[":
                arr.pop()

        elif i == ")":
            if not arr or arr[-1] == "[":
                ans = False
                break
            elif arr[-1] == "(":
                arr.pop()

    if ans and not arr:
        print("yes")
    else:
        print("no")
