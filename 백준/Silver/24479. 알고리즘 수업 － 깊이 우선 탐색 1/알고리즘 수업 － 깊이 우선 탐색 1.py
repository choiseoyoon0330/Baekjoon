import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m, r = map(int,input().split())
graph = [[] for _ in range(n+1)]
visit = [0] * (n+1)
for _ in range(m):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
    
for i in range(n+1):
    graph[i].sort()
    
c = 1     
def dfs(graph, v, visit):
    global c
    visit[v] = c
    
    for i in graph[v]:
        if visit[i] == 0:
            c += 1
            dfs(graph, i, visit)

dfs(graph, r, visit)

for i in range(1, n+1):
    print(visit[i])