import sys
from collections import deque
T = int(sys.stdin.readline())
de = deque()
for _ in range(T):
    command = list(sys.stdin.readline().strip().split())
    if command[0] == 'push_front':
        de.appendleft(int(command[1]))
    elif command[0] == 'push_back':
        de.append(int(command[1]))
    elif command[0] == 'pop_front':
        if len(de) == 0:    # 비어있으면
            print(-1)
        else:
            print(de.popleft())
    elif command[0] == 'pop_back':
        if len(de) == 0:    # 비어있으면
            print(-1)
        else:
            print(de.pop())
    elif command[0] == 'size':
        print(len(de))
    elif command[0] == 'empty':
        if len(de) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(de) == 0:
            print(-1)
        else:
            print(de[0])
    elif command[0] == 'back':
        if len(de) == 0:
            print(-1)
        else:
            print(de[-1])
