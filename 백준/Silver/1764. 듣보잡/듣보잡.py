n,m=map(int,input().split())
hear=set()
see=set()
for _ in range(n):
    name1=input()
    hear.add(name1)
for _ in range(m):
    name2=input()
    see.add(name2)
both=list(see&hear)
both.sort()
print(len(both))
for i in both:
    print(i)