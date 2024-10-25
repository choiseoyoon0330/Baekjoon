while True:
    n=int(input())
    arr=[]
    if n==-1:
        break
    for i in range(1,n):
        if n%i==0:
            arr.append(i)
    if n==sum(arr):
        b=' + '.join(map(str,arr))
        print(n,'=',b)
    else:
        print(n,"is NOT perfect.")