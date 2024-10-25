n=int(input())
a=0
arr=list(map(int,input().split()))
arr=sorted(arr)
if n%2==0:
    a=arr[0]*arr[-1]
else:
    a=arr[n//2]**2
print(a)