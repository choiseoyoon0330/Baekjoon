import sys
print = sys.stdout.write

n=int(sys.stdin.readline().rstrip())
arr=[]

for _ in range(n):
    data=int(sys.stdin.readline().rstrip())
    arr.append(data)

arr.sort()

for i in arr:
    i=str(i)
    print(i+'\n')