# +1, -1, *2 를 자식으로 두는 무한 트리로 생각했고요
# 그러다가 M만나면 그때까지 구한 누적 값(레벨) 리턴

def cal(n, m):
    q = [n]
    visited = [0] * 100001          # 최대 범위
    visited[n] = 1
    while q:
        v = q.pop(0)
        if v == m:
            return visited[v] - 1
        for x in (v - 1, v + 1, v * 2):         # 고려해야 할 3가지 경우
            if x >= 0 and x <= 100000 and visited[x] == 0:  
                q.append(x)
                visited[x] = visited[v] + 1     # 누적 합


N, M = map(int, input().split())
print(cal(N, M))