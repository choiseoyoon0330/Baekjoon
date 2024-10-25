a,b,v=map(int,input().split())
days=(v-a)/(a-b)
import math
days=math.ceil(days)
print(days+1)