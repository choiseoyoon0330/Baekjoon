n=int(input())
arr=[]
for _ in range(n):
    xy=list(map(int,input().split()))
    xy.reverse()
    arr.append(xy)
arr.sort()
for i in arr:
    i.reverse()
    print(*i)