n=int(input())
arr=[]
for _ in range(n):
    a=input()
    arr.append(a)
arr=list(set(arr))
arr.sort()
b=sorted(arr,key=len)

for i in b:
    print(i)