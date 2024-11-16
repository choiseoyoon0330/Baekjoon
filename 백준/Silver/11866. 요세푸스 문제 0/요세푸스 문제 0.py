import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int,input().split())
result = []
queue = deque([(i+1) for i in range(n)])

while queue:
    queue.rotate(-(k-1))
    result.append(queue.popleft())
print('<' + str(result).strip("[""]") + '>')
