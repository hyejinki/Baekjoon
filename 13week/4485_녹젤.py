

def f(ci, cj, sum, N):
    global minV
    dq = []
    dq.append((ci, cj))
    visited = [[0] * (N) for _ in range(N)]
    visited[ci][cj] = arr[ci][cj]
    while dq:
        i, j = dq.pop(0)
        if i == N -1 and j == N - 1:
            if minV > visited[i][j]:
                minV = visited[i][j]
        for x, y in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ni, nj = i + x, j + y
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                dq.append((ni, nj))
                visited[ni][nj] = arr[i][j] + arr[ni][nj]
                # sum += arr[ni][nj]

while True:
    N = int(input())
    if N == 0:
        break
    arr = [list(map(int, input().split()))for _ in range(N)]
    minV =  125 * 125 * 9
    f(0, 0, arr[0][0], N)
    print(minV)