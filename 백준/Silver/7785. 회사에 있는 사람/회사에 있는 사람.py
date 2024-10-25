from sys import stdin
def input():
    return stdin.readline().rstrip()
n=int(input())
dic=set()
for _ in range(n):
    a,b=input().split()
    if b=='enter':
        dic.add(a)
    else:
        dic.remove(a)
dic=sorted(dic,reverse=True)
for i in dic:
    print(i)