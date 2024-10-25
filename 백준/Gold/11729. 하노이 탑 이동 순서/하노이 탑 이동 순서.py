def htower(n,a,b):
    global cnt
    cnt+=1
    if n>1:
        htower(n-1,a,6-a-b)
        print(a,b)
        htower(n-1,6-a-b,b)
    else:
        print(a,b)
    return cnt
cnt=0
k=int(input())
print(2**k-1)
htower(k,1,3)
    