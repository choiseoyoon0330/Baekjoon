arr1=[input() for _ in range(5)]
for j in range(15):
    for i in range(5):
        if j<len(arr1[i]):
            print(arr1[i][j], end='')