n = int(input())
data = list(map(int, input().split()))

data.sort()
result = 0
k = len(data)

for i in range(k):
    result += data[i] * (k - i)
    
print(result)