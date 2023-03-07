from collections import deque

d_ij = [[0, -1, 0], [0, 0, 1], [0, 1, 0], [0, 0, -1], [-1, 0, 0], [1, 0, 0]]

def bfs(H, N, M):

    q = deque([])

    for x in coor:
        q.append((x[0], x[1], x[2], 1))
        visited[x[0]][x[1]][x[2]] = 1
    while q:
        l, r, c, v = q.popleft()
        for k in range(6):
            nl, ni, nj = l + d_ij[k][0], r + d_ij[k][1], c + d_ij[k][2]
            if 0 <= nl < H and 0 <= ni < N and 0 <= nj < M and visited[nl][ni][nj] == 0:
                q.append((nl, ni, nj, v + 1))
                visited[nl][ni][nj] = v + 1
    ans = v - 1
    for h in range(H):
        for i in range(N):
            if 0 in visited[h][i]:
                ans = -1

    return ans


M, N, H = map(int, input().split())
tmt = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
coor = []
visited = [[[0] * M for _ in range(N)] for _ in range(H)]
for h in range(H):
    for i in range(N):
        for j in range(M):
            if tmt[h][i][j] == 1:
                coor.append((h, i, j))
            if tmt[h][i][j] == -1:
                visited[h][i][j] = -1

if len(coor) == 0:
    print(-1)
else:
    print(bfs(H, N, M))