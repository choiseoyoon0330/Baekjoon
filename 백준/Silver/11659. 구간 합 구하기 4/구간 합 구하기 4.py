import sys
input=sys.stdin.readline
n,m=map(int,input().split())
N=[0]+list(map(int,input().split()))
sum_arr=[]
temp=0
for a in N:
    temp+=a
    sum_arr.append(temp)
for _ in range(m):
    i,j=map(int,input().split())
    print(sum_arr[j]-sum_arr[i-1])