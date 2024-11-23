import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
ans = -1

for _ in range(m):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
    
for i in graph:
    i.sort()
    
c = 1
def dfs(graph, r, visited):
    global c
    visited[r] = c
    for i in graph[r]:
        if not visited[i]:
            c += 1
            dfs(graph, i, visited)
            
dfs(graph, 1, visited)

for i in visited[1:]:
    if i:
        ans += 1

print(ans)