from heapq import heappush
from heapq import heappop
import sys
input=sys.stdin.readline
n=int(input())
stack=[]
for _ in range(n):
    x=int(input())
    x_abs=abs(x)
    if x!=0:
        heappush(stack,(x_abs,x))
    else:
        try:
            A=heappop(stack)
            print(A[1])
        except:
            print(0)