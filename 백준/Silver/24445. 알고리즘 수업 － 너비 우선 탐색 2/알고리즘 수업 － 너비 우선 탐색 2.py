import sys
from collections import deque
input = sys.stdin.readline

n, m, r = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
    
for i in graph:
    i.sort(reverse = True)

def bfs(graph, r, visited):
    queue = deque([r])
    visited[r] = 1
    c = 2
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = c
                c += 1

bfs(graph, r, visited)
for i in visited[1:]:
    print(i)