from heapq import heappush,heappop
import sys
input=sys.stdin.readline

n=int(input())
stack=[]
for _ in range(n):
    x=int(input())
    if x!=0:
        heappush(stack,(-x,x))
    else:
        if stack:
            print(heappop(stack)[1])
        else:
            print(0)