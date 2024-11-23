import sys
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
    i.sort(reverse = True)
    
c = 1
def dfs(v):
    global c
    visited[v] = c
    for i in graph[v]:
        if visited[i]:
            continue
        c += 1
        dfs(i)
    
dfs(r)
for i in visited[1:]:
    print(i)