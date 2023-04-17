

def f(ci, cj, sum):
    global minV
    if sum > minV:
        return
    if ci == N - 1 and cj == N - 1:
        if minV > sum:
            minV = sum
    else:
        for i, j in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ni, nj = ci + i, cj + j
            if 0 <= ni < N and 0 <= nj < N:
                f(ni, nj, sum+arr[ni][nj])







while True:
    N = int(input())
    if N == 0: 
        break
    arr = [list(map(int, input().split()))for _ in range(N)]
    minV =  125 * 125 * 9
    print(f(0, 0, arr[0][0]))
    print(minV)