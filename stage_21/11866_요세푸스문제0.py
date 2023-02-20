import sys
from collections import deque
N, K = map(int,sys.stdin.readline().strip().split())
arr = deque()
ans = ''
for i in range(1, N+1):
    arr.append(i)
while True:
    for _ in range(N-1):
        arr.append(arr.popleft())       # N-1개는 왼쪽에서 pop, 오른쪽에 삽입
    ans += str(arr.popleft())        # N번째는 pop
    if len(arr) < N:
        for i in arr:
            ans += str(i)
        break
print(ans)

    


