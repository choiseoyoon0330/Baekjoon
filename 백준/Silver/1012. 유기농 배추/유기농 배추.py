from collections import deque

t = int(input())
    
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = cnt
                    queue.append((nx, ny))
    return cnt
    
data = []                
for _ in range(t):
    cnt = 2
    result = 0
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                graph[i][j] = cnt
                result = max(result, bfs(i, j))
                cnt += 1       
    data.append(result - 1)   
    
for i in data:
    print(i)