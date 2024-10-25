import sys
import math
def is_prime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return False
    return True
t=int(sys.stdin.readline())
for _ in range(t):
    n=int(sys.stdin.readline())
    while True:
        if n==0 or n==1:
            print(2)
            break
        elif is_prime(n):
            print(n)
            break
        else:
            n+=1

