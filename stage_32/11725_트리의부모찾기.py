from collections import deque
def bfs(N):
    dq = deque([1])         # 1을 루트로 시작혀
    visited = [0]*(N + 1)
    visited[1] = 1
    while dq:
        x = dq.popleft()
        for i in tree[x]:
            if visited[i] == 0:         # 방문 안했으면
                ans[i] = x              # 자식 번호에 부모 넣는다.
                dq.append(i)
                visited[i] = 1


N = int(input())
tree = [[] for _ in range(N+1)] 
ans = [0] * (N + 1)             # 자식을 인덱스로 value는 부모
for _ in range(N - 1):
    v, w = map(int, input().split())
    tree[v].append(w)       # 양방향
    tree[w].append(v)

bfs(N)
for i in range(2, N + 1):
    print(ans[i])