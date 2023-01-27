# 행렬 덧셈

# 입력 받은 두 숫자로 NxM크기의 2차원 배열을 만든다.
N, M = map(int, input().split())
A = []
for n in range(2):  # 2개의 배열
    mylist = [list(map(int, input().split())) for _ in range(N)]
    if n == 0:
        A = mylist  # A에 저장해둠
for i in range(N):
    for j in range(M):
        A[i][j] += mylist[i][j] # A에 mylist를 더함
    print(*A[i])


