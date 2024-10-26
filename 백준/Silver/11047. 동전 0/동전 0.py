import sys
input = sys.stdin.readline

n, k = map(int,input().split())
wallet = []
cnt = 0
for _ in range(n):
    coin = int(input())
    wallet.append(coin)
wallet = reversed(wallet)
for j in wallet:
    cost = k // j
    if cost > 0:
        cnt += cost
        k %= j
    else:
        continue;
print(cnt)