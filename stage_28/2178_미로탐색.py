d_ij = [[-1, 0], [0, 1], [1, 0], [0, -1]]       # 위부터 시계방향
N, M = map(int, input().split())
arr = [list(map(int, input()))for _ in range(N)]
visited = [[0] * M for _ in range(N)]
q = [(0, 0)]                # 좌표를 담을 큐
visited[0][0] = 1
while len(q):
    coor = q.pop(0)
    r, c = coor[0], coor[1]
    for k in range(4):
        ni, nj = r + d_ij[k][0], c + d_ij[k][1]
        if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and arr[ni][nj] == 1:
            q.append((ni, nj))
            visited[ni][nj] = visited[r][c] + 1
print(visited[N-1][M-1])



