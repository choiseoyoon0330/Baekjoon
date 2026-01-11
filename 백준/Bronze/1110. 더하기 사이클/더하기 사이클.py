n = int(input())
original = n
cnt = 0

while True:
    tens = n // 10
    ones = n % 10
    new_ones = (tens + ones) % 10
    n = ones * 10 + new_ones
    cnt += 1
    
    if original == n:
        break

print(cnt)