s=input()
arr=set()
for i in range(1,len(s)+1):
    for j in range(len(s)+1-i):
        arr.add(s[j:i+j])
print(len(arr))