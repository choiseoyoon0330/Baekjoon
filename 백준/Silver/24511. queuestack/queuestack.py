import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
m = int(input())
c = list(map(int,input().split()))

queue = deque([])
for i in range(n):
    if a[i] == 0:
        queue.appendleft(b[i])
if not queue:
    print(*c)
else:
    for i in range(m):
        queue.append(c[i])
        print(queue.popleft(), end = " ")