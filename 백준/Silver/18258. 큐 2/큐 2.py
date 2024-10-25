import sys
input=sys.stdin.readline
from collections import deque
n=int(input())
deck=deque([])

for _ in range(n):
    command=list(input().split())
    if command[0]=='push':
        deck.append(int(command[1]))
    elif command[0]=='pop':
        if deck:
            print(deck.popleft())
        else:
            print(-1)
    elif command[0]=='size':
        print(len(deck))
    elif command[0]=='empty':
        if deck:
            print(0)
        else:
            print(1)
    elif command[0]=='front':
        if deck:
            print(deck[0])
        else:
            print(-1)
    else:
        if deck:
            print(deck[-1])
        else:
            print(-1)