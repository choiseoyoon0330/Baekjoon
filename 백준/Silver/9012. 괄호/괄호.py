n=int(input())
stack=[]
ans=0
for _ in range(n):
    word=input()
    for i in word:
        if i=='(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                ans='NO'
                break
        if stack:
            ans="NO"
        else:
            ans="YES"
    print(ans)
    stack=[]