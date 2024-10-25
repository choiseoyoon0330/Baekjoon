n=input()
arr=[]
for i in range(len(n)):
    arr.append(int(n[i]))
arr=sorted(arr,reverse=True)
for i in range(len(arr)):
    print(arr[i],end='')