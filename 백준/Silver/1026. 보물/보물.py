n=int(input())
s=0
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=sorted(b)
a.sort(reverse=True)

for i in range(n):
    s+=a[i]*c[i]
print(s)