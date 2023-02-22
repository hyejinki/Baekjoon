import sys
from collections import deque
T = int(sys.stdin.readline())
for _ in range(T):
    p = str(sys.stdin.readline().strip())            # 수행할 함수
    n = int(sys.stdin.readline())       # 배열 크기
    arr = deque(sys.stdin.readline().strip('[').strip().strip(']').split(','))
    print(type(arr))
    for i in range(len(p)):
        if p[i] == 'R':     # 순서 뒤집기
            arr.reverse()
    
        else:               # 맨 앞 삭제
            if len(arr) ==1:
                arr = 'error'  
              
            else:
                arr.popleft()
    print('['+','.join(arr)+ ']')