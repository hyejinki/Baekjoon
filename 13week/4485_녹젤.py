import heapq

INF =  125 * 125 * 9
t = 0
while True:
    t += 1
    N = int(input())
    if N == 0: 
        break
    arr = [list(map(int, input().split()))for _ in range(N)]
    dis = [[INF] * N for _ in range(N)]
    hq = [(arr[0][0], 0, 0)]
    dis[0][0] = arr[0][0]
    while hq:
        cost, x, y = heapq.heappop(hq)
        # if dis[x][y] < cost:
        #     continue
        # else:
        for i in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ni, nj = x + i[0] , y + i[1]
            if 0 <= ni < N and 0 <= nj < N:
                n_cost = cost + arr[ni][nj]
                if dis[ni][nj] > n_cost:
                    dis[ni][nj] = n_cost
                    heapq.heappush(hq, (n_cost, ni, nj))
    
    print(f'Problem {t}: {dis[N-1][N-1]}')