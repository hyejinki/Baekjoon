def f(arr, i, t, N):      #  행렬, 시작, 합, N
    global minV
    if t > minV:
        return
    if i > N:
        if minV > t:
            minV = t
        return t
    else:
        if arr[i][1] <= arr[i + 1][0]:
            f(arr, i + 1, t + arr[i][2] + arr[i+ 1][0] - arr[i][1], N)
            f(arr, i + 1, t + arr[i][1] - arr[i][0] , N)
        else:
            f(arr, i + 1, t + arr[i][1] - arr[i][0] , N)

N, D = map(int, input().split())
arr = [[0, 0, 0]] + [list(map(int, input().split()))for _ in range(N)]
print(arr)
arr.sort()
minV = 10000
t = 0
f(arr,0, t, N + 1)
print(minV)