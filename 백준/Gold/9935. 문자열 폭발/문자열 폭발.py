import sys
input=sys.stdin.readline
line=list(input().strip())
bomb=list(input().strip())
m=len(bomb)
stack=[]
for i in line:
    stack.append(i)
    if stack[-1]==bomb[-1] and stack[len(stack)-m:len(stack)]==bomb:
        for _ in range(m):
            stack.pop()
if stack:
    print(*stack,sep='')
else:
    print('FRULA')