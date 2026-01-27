from collections import deque
n = int(input())
graph = []
result = []
for _ in range(n):
    graph.append(list(map(int, input().strip())))
    
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
town = 2

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = town
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = town
                    queue.append((nx, ny))
                    cnt += 1
                    
    return cnt

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            result.append(bfs(i, j))
            town += 1
            
print(len(result))
for cnt in sorted(result):
    print(cnt)