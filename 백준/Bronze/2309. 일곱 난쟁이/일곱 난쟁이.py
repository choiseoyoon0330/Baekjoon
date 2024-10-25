import random
arr=[]
for _ in range(9):
    arr.append(int(input()))
while True:
    choice=random.sample(arr,7)
    choice.sort()
    total=sum(choice)
    if total==100:
        print(*choice,end='')
        break