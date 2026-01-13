from itertools import combinations
from collections import deque

n, m = map(int, input().split())
graph = []
space = []
virus = []

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if graph[i][j] == 0:
            space.append((i, j))
        elif graph[i][j] == 2:
            virus.append((i, j))

def spread_virus(temp):
    queue = deque(virus)
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >=0 and ny < m:
                if temp[nx][ny] == 0:
                    temp[nx][ny] = 2
                    queue.append((nx, ny))
                
            
def get_score(temp):
    return sum(row.count(0) for row in temp) 

result = 0

for walls in combinations(space, 3):
    temp = [row[:] for row in graph]
    for x, y in walls:
        temp[x][y] = 1
    spread_virus(temp)
    result = max(result, get_score(temp))

print(result)
    