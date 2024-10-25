n=int(input())
word=[]
for i in range(n):
    word.append(input())
for j in word:
    for k in range(len(j)-1):
        if j[k]==j[k+1]:
            pass
        elif j[k] in j[k+1:]:
            n-=1
            break
print(n)