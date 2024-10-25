import sys
input=sys.stdin.readline
d={}
n,m=map(int,input().split())
for _ in range(n):
    word=input().rstrip()
    if len(word)<m:
        continue
    if d.get(word):
        d[word][0]+=1
    else:
        d[word]=[1,len(word),word]
ans=sorted(d.items(),key=lambda x:(-x[1][0],-x[1][1],x[1][2]))
for i in ans:
    print(i[0])