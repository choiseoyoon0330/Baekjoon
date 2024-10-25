import sys
n=int(sys.stdin.readline().rstrip())
arr=list(map(int,sys.stdin.readline().rstrip().split(' ')))
arr2=sorted(list(set(arr)))
arr_dict={arr2[i]:i for i in range(len(arr2))}

for i in arr:
    print(arr_dict[i],end=' ')