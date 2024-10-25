import sys

n=int(sys.stdin.readline().rstrip())
arr=[]
dic={}
for _ in range(n):
    num=int(sys.stdin.readline().rstrip())
    arr.append(num)
    if num in dic:
        dic[num]+=1
    else:
        dic[num]=1

arr.sort()
maxnum=0
for i in dic.keys():
    if dic[i]>maxnum:
        maxnum=dic[i]
arr2=[]
for j in dic.keys():
    if dic[j]==maxnum:
        arr2.append(j)
arr2.sort()
if len(arr2)==1:
    c=arr2[0]
else:
    c=arr2[1]


a=round(sum(arr)/n)
b=arr[n//2]
d=max(arr)-min(arr)

sys.stdout.write(str(a)+'\n'+str(b)+'\n'+str(c)+'\n'+str(d))