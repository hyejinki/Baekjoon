import sys
from collections import deque

N, K = map(int, sys.stdin.readline().strip().split())
arr = deque()
ans = []                # 정답을 담을 리스트
for i in range(1, N + 1):
    arr.append(i)
while True:
    if len(arr) == 1:  # arr에 남은 게 하나면 바로 ans행
        ans.append(str(arr[0]))
        break
    for _ in range(K - 1):          # K-1개는 왼쪽에서 pop, 오른쪽에 삽입
        arr.append(arr.popleft())  
    ans.append(str(arr.popleft()))  # N번째는 pop, ans에 넣어줘

print('<' + ', '.join(ans) + '>')
