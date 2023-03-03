d_ij = [[-1, 0], [0, 1], [1, 0], [0, -1]]       # 위부터 시계방향
N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
counts = 0      # 단지 수
ans = []        # 단지내 집의 수
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:      # 1을 찾아서
            q = [(i, j)]        # 좌표 넣고
            arr[i][j] = 0       # 0 으로 만들고
            sum_v = 1           # 집 ++
            while len(q):
                coor = q.pop(0)
                r, c = coor[0], coor[1]     # 좌표 r, c
                for k in range(4):
                    ni, nj = r + d_ij[k][0], c + d_ij[k][1]
                    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj]: # 지나온 건 0으로 만들었으니까 1만 찾아
                        q.append((ni, nj))
                        arr[ni][nj] = 0
                        sum_v += 1

            counts += 1
            ans.append(sum_v)
            ans.sort()          # 오름차순!!!!!!!!!!!!!!

print(counts)
print(*ans,sep='\n')



