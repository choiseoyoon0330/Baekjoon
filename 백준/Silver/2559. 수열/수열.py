import sys
input = sys.stdin.readline
n, k = map(int,input().split())
temp = list(map(int, input().split()))
temp_add = []
temp_sum = sum(temp[0:k])
temp_add.append(temp_sum)
if n==k:
    print(temp_sum)
else:
    for i in range(1, n-k+1):
        temp_sum = temp_sum - temp[i-1] + temp[i+k-1]
        temp_add.append(temp_sum)
    print(max(temp_add))