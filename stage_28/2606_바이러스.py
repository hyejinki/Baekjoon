N = int(input())
M = int(input())
adjL = [[]for _ in range(N + 1)]
for _ in range(M):
    v, w = map(int,input().split())
    adjL[v].append(w)
    adjL[w].append(v)

q = [1]         # 시작점이 1로 정해져있으니
visited = [0] * (N + 1)
visited[1] = 1

while len(q):
    i = q.pop(0)        # 팝팝팝
    for x in adjL[i]:
        if visited[x] == 0:     # 방문하지 않은 곳이라면
            q.append(x)
            visited[x] = 1

print(visited.count(1) - 1)     # 처음 1은 빼요