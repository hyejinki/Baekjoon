from collections import deque
def bfs(start, V):
    dq = deque()
    dq.append((1, 0))
    visited = [-1] * (V+1)
    visited[start] = 0

    while dq:
        x, d = dq.popleft()
        for i in info[x]:
            if visited[i[0]] == -1:
                dq.append(i)
                visited[i[0]] = d + i[1]
        print(visited)
    return max(visited)


V = int(input())
info = [[] for _ in range(V + 1)]
for _ in range(V):
    temp = list(map(int, input().split()))
    v = temp[0]
    for i in range(1, len(temp), 2):
        if temp[i] == -1:
            break
        else:
            info[v].append((temp[i], temp[i+1]))

print(bfs(1, V))