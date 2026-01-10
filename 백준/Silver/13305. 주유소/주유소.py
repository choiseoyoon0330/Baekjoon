import sys
input = sys.stdin.readline

n = int(input())
road = list(map(int, input().split()))
oil = list(map(int, input().split()))

result = 0
min_oil = oil[0]
for i in range(n - 1):
    if oil[i] < min_oil:
        min_oil = oil[i]
    result += min_oil * road[i]
    
print(result)