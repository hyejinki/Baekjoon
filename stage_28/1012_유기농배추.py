d_ij = [[-1, 0], [0, 1], [1, 0], [0, -1]]       # 위부터 시계방향
T = int(input())
for tc in range(T):
    M, N, K = map(int, input().split())
    baechu = []                        # 배추 리스트
    counts = 0
    for _ in range(K):
        y, x = map(int, input().split())    # 순서 주의!
        baechu.append((x, y))           # 좌표

    while len(baechu):
        q = [(baechu[0])]
        baechu.remove((baechu[0]))      # 확인한 좌표는 없애줄 거임
        while len(q):
            coor = q.pop()
            r, c = coor[0], coor[1]  # 좌표 r, c
            for k in range(4):
                ni, nj = r + d_ij[k][0], c + d_ij[k][1]
                if 0 <= ni < N and 0 <= nj < M and (ni, nj) in baechu:   # 배추 리스트에 있는 좌표라면 ok
                    q.append((ni, nj))                  # 살펴볼 좌표 푸시
                    baechu.remove((ni, nj))             # 배추리스트에서 없애
        counts += 1
    print(counts)
