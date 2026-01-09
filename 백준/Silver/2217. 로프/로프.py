n = int(input())
data = []
for i in range(n):
    data.append(int(input()))
    
max_weight = 0
data.sort(reverse = True)
for i in range(n):
    weight = data[i] * (i + 1)
    if max_weight < weight:
        max_weight = weight
print(max_weight)