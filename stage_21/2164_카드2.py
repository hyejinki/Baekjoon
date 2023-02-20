from collections import deque

N = int(input())
dec = deque([])
for i in range(N):              # 숫자카드 넣어준다
    dec.append(i+1)
while len(dec) != 1:            # 한 개 남을 때까지
    dec.popleft()               # 하나 버리고
    dec.append(dec.popleft())   # 왼쪽에서 버린 거 오른쪽에 추가

print(*dec)