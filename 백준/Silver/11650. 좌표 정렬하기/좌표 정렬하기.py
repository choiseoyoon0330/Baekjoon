n=int(input())
arr=[]
for _ in range(n):
    xy=list(map(int,input().split()))
    arr.append(xy)
arr.sort()
for i in arr:
    print(*i)