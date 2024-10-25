from collections import Counter
n=int(input())
card=list(map(int,input().split()))
m=int(input())
check=list(map(int,input().split()))
count=Counter(card)
for i in check:
    if i in count:
        print(count[i],end=' ')
    else:
        print(0,end=' ')