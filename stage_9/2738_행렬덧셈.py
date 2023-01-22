# 행렬 덧셈
N, M = map(int, input().split())
A = []
for n in range(2):
    mylist = [list(map(int, input().split())) for _ in range(N)]
    if n == 0:
        A = mylist  # A에 저장해둠
for i in range(N):
    for j in range(M):
        A[i][j] += mylist[i][j] # A에 mylist를 더함
    print(*A[i])


