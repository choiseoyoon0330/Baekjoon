import sys
input = sys.stdin.readline

data = [300, 60, 10]
result = [0] * 3

t = int(input())

if t % 10 != 0:
    print(-1)
else:
    while True:
        if t == 0:
            break
        for i in range(3):
            result[i] = t // data[i]
            t %= data[i]
    print(*result)
