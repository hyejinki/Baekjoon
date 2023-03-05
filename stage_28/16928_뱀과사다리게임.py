from collections import deque
def bfs():
    dq = deque([1])
    visited = [0] * 101
    visited[1] = 1
    while dq:
        i = dq.popleft()
        if i == 100:                    # 종료 조건
            return visited[i] - 1
        for k in range(1, 7):           # 주사위 1 ~ 6
            if i + k in dic:
                x = dic[i + k]          # 딕셔너리에 있는 값이면 value를 x로
            else:
                x = i + k
            if 1<= x <= 100 and visited[x] == 0:
                dq.append(x)
                visited[x] = visited[i] + 1

N, M = map(int, input().split())
dic = {}                    # 사다리, 뱀 시작 위치를 key, 도착 위치를 value
for _ in range(N+M):
    x1, x2 = map(int, input().split())
    dic[x1] = x2
print(bfs())