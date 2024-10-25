import sys
input=sys.stdin.readline
n=int(input())
cnt=0
s=set()
for _ in range(n):
    chat=input()
    if chat=='ENTER\n':
        cnt+=len(s)
        s=set()
    else:
        s.add(chat)
cnt+=len(s)
print(cnt)