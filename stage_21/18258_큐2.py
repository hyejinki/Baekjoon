import sys
from collections import deque
N = int(input())
dec = deque()
for _ in range(N):
    command = list(sys.stdin.readline().strip().split())
    if command[0] == 'push':
        dec.append(int(command[1]))
    elif command[0] == 'pop':
        if len(dec) == 0:           # 비어있으면
            print(-1)
        else:
            print(dec.popleft())    
    elif command[0] == 'size':
        print(len(dec))
    elif command[0] == 'empty':
        if len(dec) == 0:           # 비어있으면
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(dec) == 0:           # 비어있으면
            print(-1)
        else:
            print(dec[0])           # 맨 앞
    elif command[0] == 'back':
        if len(dec) == 0:           # 비어있으면
            print(-1)
        else:
            print(dec[-1])          # 맨 뒤