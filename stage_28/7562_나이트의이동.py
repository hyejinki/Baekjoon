# 8방향으로 다 볼 거임
# visited 누적합을 출력

# 오른쪽 대각선 부터 시계방향
d_ij = [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]
def find(N, s1, s2, f1, f2):
    q = [(s1, s2)]
    visited = [[0] * N for _ in range(N)]
    visited[s1][s2] = 1
    while q:
        coor = q.pop(0) 
        r, c = coor[0], coor[1]
        if r == f1 and c == f2:             # 종료 조건
            return visited[r][c] - 1
        for k in range(8):
            ni, nj = r + d_ij[k][0], c + d_ij[k][1]
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[r][c] + 1


T = int(input())
for test_case in range(T):
    I = int(input())
    s1, s2 = map(int, input().split())          # 시작 좌표
    f1, f2 = map(int, input().split())          # 목적지 좌표
    print(find(I, s1, s2, f1, f2))