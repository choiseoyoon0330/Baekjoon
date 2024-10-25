import sys
from collections import Counter

n=int(input())
arr=list(map(int,input().split()))
q=int(input())

for _ in range(q):
    query=list(map(int,input().split()))
    count=Counter(arr[query[1]-1:query[2]] )
    if query[0]==1:
        print(count[query[3]])
    else:
        arr[query[1]-1:query[2]]=[0]*(query[2]-(query[1]-1))