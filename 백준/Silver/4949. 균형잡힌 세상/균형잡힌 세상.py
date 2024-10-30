import sys
input = sys.stdin.readline

while (True):
    line = input().rstrip('\n')
    ans = "yes"
    if line == ".":
        break
    stack = []
    for i in line:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == ")":
            if stack and stack[-1] == "(" :
                stack.pop()
            else:
                ans = "no"
                break
        elif i == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                ans = "no"
                break
        else:
            continue
    if stack:
        ans = "no"
    print(ans)
    