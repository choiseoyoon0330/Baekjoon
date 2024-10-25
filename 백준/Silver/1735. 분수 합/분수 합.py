import math
a,b=map(int,input().split())
c,d=map(int,input().split())
n=math.gcd((a*d)+(b*c),b*d)
print(((a*d)+(b*c))//n,(b*d)//n,end='')