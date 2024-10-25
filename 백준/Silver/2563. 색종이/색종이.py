n=int(input())
ss=[[0 for _ in range(100)]for _ in range(100)]

for i in range(n):
    a,b=map(int,input().split())
    for j in range(a,a+10):
        for k in range(b,b+10):
            ss[j][k]=1
            
cnt=0
for i in ss:
    cnt+=i.count(1)
print(cnt)