import sys
import math

n=int(sys.stdin.readline())
first=int(sys.stdin.readline())
space=[]

for i in range(n-1):
    num=int(sys.stdin.readline())
    space.append(num-first)
    first=num
    
g=math.gcd(*space)

result=0

for each in space:
    result+=((each//g)-1)

print(result)