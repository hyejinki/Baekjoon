import sys
from collections import deque
T = int(sys.stdin.readline())
for _ in range(T):
    p = sys.stdin.readline()            # 수행할 함수
    n = int(sys.stdin.readline())       # 배열 크기
    arr = deque(list(map(int, sys.stdin.readline().strip('[]\n'+'').split(','))))
   
    for i in range(len(p)):
        if p[i] == 'R':     # 순서 뒤집기
            last = arr[-1]  # arr 마지막 숫자 기억하고
            while last != arr[0]:   # 마지막 숫자가 arr 맨 앞에 올 때까지
                arr.append(arr.popleft())   # 왼쪽으로 shift
        else:               # 맨 앞 삭제
            arr.popleft()
    print(arr)