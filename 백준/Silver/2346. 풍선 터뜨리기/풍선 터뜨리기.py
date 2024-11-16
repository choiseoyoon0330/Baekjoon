import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
queue = deque(enumerate(map(int,input().split())))
ans = []

while queue:
    idx, paper = queue.popleft()
    ans.append(idx + 1)
    if paper > 0:
        queue.rotate(-(paper - 1))
    else:
        queue.rotate(-paper)
print(*ans)