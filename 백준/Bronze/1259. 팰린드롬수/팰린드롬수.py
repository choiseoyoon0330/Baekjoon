while True:
    line=input()
    if line=='0':
        break
    line=list(line)
    if line[::]==line[::-1]:
        print('yes')
    else:
        print('no')