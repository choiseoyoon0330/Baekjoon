import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
num = list(map(int,input().split()))
queue = deque(list(range(1, n+1)))
cnt = 0

for i in num:
    if queue.index(i) <= (len(queue) // 2):
        cnt += queue.index(i)
        queue.rotate(-queue.index(i))
        queue.popleft()
    else:
        cnt += (len(queue) - queue.index(i))
        queue.rotate(len(queue) - queue.index(i))
        queue.popleft()

print(cnt)