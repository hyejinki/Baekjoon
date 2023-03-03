def bfs(v, N):
    q = [v]
    visited = [0] * (N + 1)
    visited[v] = 1
    ans = []
    while len(q):
        i = q.pop(0)
        ans.append(i)
        for x in arr[i]:
            if visited[x] == 0:
                visited[x] = 1
                q.append(x)
    return ans

def dfs(V, N):
    visited = [0] * (N + 1)
    stack = []
    ans = [V]
    v = V
    while True:
        visited[v] = 1
        for x in arr[v]:
            if visited[x] == 0:
                visited[x] = 1
                stack.append(v)
                ans.append(x)
                v = x
                break
        else:
            if stack:
                v = stack.pop()
            else:
                break
    return ans

N, M, V = map(int, input().split())
adjL = [[] for _ in range(N + 1)]
for _ in range(M):
    v, w = map(int, input().split())
    adjL[v].append(w)
    adjL[w].append(v)

arr = [[] for _ in range(N + 1)]
for i in range(N+1):
    arr[i] = sorted(adjL[i])

print(*dfs(V, N))
print(*bfs(V, N))

