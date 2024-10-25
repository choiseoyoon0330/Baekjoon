from sys import stdin
def input():
    return stdin.readline().rstrip()

n,m=map(int,input().split())
dic_num={}
dic_name={}
for i in range(1,n+1):
    name=input()
    dic_name[name]=i
    dic_num[i]=name

for _ in range(m):
    qst=input()
    if qst.isdigit():
        print(dic_num[int(qst)])
    else:
        print(dic_name[qst])