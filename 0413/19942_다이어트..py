# def f(p, fv, s, v, cost):
#     global minV
#     if minV < cost:
#             return
#     if p >= mp and fv >= mf and s >= ms and v >= mv:
#         if minV > cost:
#             minV = cost
    
#     else:
#         # 더하거나
#         for i in range(N):
#             f(p + arr[i][0], fv + arr[i][1], s + arr[i][2], v + arr[i][3], cost + arr[i][4])
#         # 넘기거나
#             f(p, fv, s, v, cost)
#     return


# import sys
# N = int(sys.stdin.readline())
# mp, mf ,ms, mv = map(int, sys.stdin.readline().split())
# arr = [list(map(int, sys.stdin.readline().split()))for _ in range(N)]
# print(arr)
# minV = 500 * N
# f(0, 0, 0, 0, 0)
# print(minV)