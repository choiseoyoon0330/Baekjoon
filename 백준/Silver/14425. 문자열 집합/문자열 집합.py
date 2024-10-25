n,m=map(int,input().split())
s=set()
c=[]
cnt=0
for _ in range(n):
    word=input()
    s.add(word)
for _ in range(m):
    check=input()
    c.append(check)
for i in c:
    if i in s:
        cnt+=1
print(cnt)