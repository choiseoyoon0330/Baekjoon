import math
t=int(input())

for _ in range(t):
    am=1
    a,b=map(int,input().split())
    for i in range(a):
        am*=(b-i)
    print(am//math.factorial(a))