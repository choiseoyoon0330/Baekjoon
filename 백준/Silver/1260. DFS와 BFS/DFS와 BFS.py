import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m, r = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
    
for i in graph:
    i.sort()
    
graph_bfs = graph.copy()
visited_bfs = visited.copy()
   
c = 1 
def dfs(graph, r, visited):
    global c
    visited[r] = c
    print(r, end = ' ')
    for i in graph[r]:
        if not visited[i]:
            c += 1
            dfs(graph, i, visited)
            
def bfs(graph, r, visited):
    queue = deque([r])
    visited[r] = 1
    c = 2
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = c
                c += 1
    
dfs(graph, r, visited)
print()
bfs(graph_bfs, r, visited_bfs)