n = int(input())
data = []
for i in range(n):
    start, end = map(int, input().split())
    data.append((end, start))
    
data.sort()
result = 0
end_time = 0

for end, start in data:
    if start >= end_time:
        end_time = end
        result += 1
print(result)