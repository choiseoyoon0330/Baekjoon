from heapq import heappush
from heapq import heappop
import sys
input=sys.stdin.readline

n=int(input())
stack=[]
for _ in range(n):
    x=int(input())
    if x!=0:
        heappush(stack,x)
    else:
        if stack:
            print(heappop(stack))
        else:
            print(0)