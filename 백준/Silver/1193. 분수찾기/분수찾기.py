import sys
x=int(sys.stdin.readline())
line=1
while x>line:
    x-=line
    line+=1
if line%2!=0:
    a=line-x+1
    b=x
else:
    a=x
    b=line-x+1
print(f'{a}/{b}')