import sys
from collections import deque
N, M = map(int, sys.stdin.readline().strip().split())
deq = deque()
for i in range(N):          # 크기 N만큼의 덱
    deq.append(i+1)
num = list(map(int, sys.stdin.readline().strip().split()))

count = 0
for x in num:
    for i in range(len(deq)):       # deq에서의 x의 인덱스 찾는 과정
        if x == deq[i]:
            break
    if x == deq[0]:
        deq.popleft()
    elif i <= (len(deq) // 2):            # 가운데보다 앞에 있다면
        # 2번
        while deq[0] != x:
            count += 1
            deq.append(deq.popleft())     # 왼쪽으로 shift
        deq.popleft()               # pop
    else:
        # 3번
        while deq[0] != x:
            count += 1
            deq.appendleft(deq.pop())     # 오른쪽으로 shift
        deq.popleft()  # pop
print(count)