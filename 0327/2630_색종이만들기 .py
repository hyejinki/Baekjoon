
def check(si, ei, sj, ej):
    pass


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

check(0, N // 2, 0, N//2)
check(0, N // 2, N // 2, N)
check( N // 2, N, 0, N//2)
check( N // 2, N,  N // 2, N)

