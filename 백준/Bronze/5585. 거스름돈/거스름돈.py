n = int(input())
data = [500, 100, 50, 10, 5, 1]

result = 0
k = 1000 - n
while True:
    if k == 0:
        break
    else:
        for i in data:
            result += k // i
            k %= i
print(result)