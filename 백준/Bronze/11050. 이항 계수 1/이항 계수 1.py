n,k=map(int,input().split())
nm=1
km=1
for i in range(k):
    nm*=(n-i)
for j in range(k):
    km*=(k-j)
print(nm//km)