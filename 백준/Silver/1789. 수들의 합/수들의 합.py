import sys
input = sys.stdin.readline

s = int(input())
k = 0

while s >= k + 1:
    k += 1
    s -= k
    
print(k)