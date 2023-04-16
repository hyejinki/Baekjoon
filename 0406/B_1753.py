import sys
import heapq

def f(start):
    heap = []
    heapq.heappush(heap, (0, start))
    while heap:
        sum, no = heapq.heappop(heap)
        if adjM[no] < sum:
            continue
        for w, next_n in adjM[no]:
            next_w = w + sum
            if next_w < w_table[next_n]:
                w_table[next_n] = next_w
                heapq.heappush(heap,(next_w, next_n))
                

INF = 100000000
V, E = map(int, input().split())
start = int(input())
adjM = [[0] *(V+1) for _ in range(V+1)]
w_table = [INF] * (V + 1)
w_table[start] = 0
for _ in range(E):
    u, v, w = map(int, input().split())
    adjM[u][v] = w
f(1)
print(adjM)