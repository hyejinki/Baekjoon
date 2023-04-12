# This is a sample Python script.
import heapq
def f(start):
    heap = []
    heapq.heappush(heap, (0, start))

    while heap:

        sum, no = heapq.heappop(heap)
        for n_node, w in adjL[no]:
            next_w = w + sum
            if next_w < wt[n_node]:
                wt[n_node] = next_w
                heapq.heappush(heap, (next_w, n_node))
    return


V, E = map(int, input().split())
s = int(input())
INF = 10 * V + 1
wt = [INF] * (V + 1)
wt[s] = 0
adjL = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    adjL[u].append((v, w))

f(s)

for i in range(1, V + 1):
    if wt[i] == INF:
        print('INF')
    else:
        print(wt[i])