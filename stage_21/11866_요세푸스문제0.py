import sys
from collections import deque
N, K = map(int,sys.stdin.readline().strip().split())
arr = deque()
ans = ''
for i in range(1, N+1):
    arr.append(i)
while True:
    for _ in range(K-1):
        arr.append(arr.popleft())       # K-1개는 왼쪽에서 pop, 오른쪽에 삽입
    ans += str(arr.popleft())        # N번째는 pop
    if len(arr) < K:
        for i in arr:               # arr에 남은 것들을 ans에 더해줌
            ans += str(i)
        break
print('<' + ', '.join(ans) + '>')
