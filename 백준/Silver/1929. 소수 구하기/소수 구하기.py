import sys
import math
m,n=map(int,sys.stdin.readline().split())

for i in range(m,n+1):
    if i==1:
        continue
    for j in range(2,int(math.sqrt(i))+1):
        if i%j==0:
            break
    else:
        print(i)