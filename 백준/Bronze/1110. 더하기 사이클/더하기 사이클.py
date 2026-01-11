n = input()
result = 0

if len(n) == 1:
    n = str(0) + n
    
new = n
while True:
    add_num = str(int(new[0]) + int(new[1]))
    new = new[1] + add_num[-1]
    result += 1
    if new == n:
        break
    
    
print(result)