infix = input()
stack = []
ans = ''
sym = {
    '(' : 0,
    '*' : 2,
    '/' : 2,
    '+' : 1,
    '-' : 1,
}
for token in infix:
    if 'A' <= token <= 'Z':
        ans += token
    else:
        if not stack:
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.pop()
        else:
            while stack and sym[token] <= sym[stack[-1]]:
                ans += stack.pop()
            stack.append(token)
while stack:
    ans += stack.pop()
print(ans)