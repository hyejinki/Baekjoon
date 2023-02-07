def binarysearch(arr, N, M):
    start = 0
    end = N-1
    while start <= end:
        middle = (start + end)//2
        if arr[middle] == M:
            return M
        elif arr[middle] > M:
            end = middle - 1
        else:
            start = middle + 1
    

N, M = map(int, input().split())
for _ in range(N):
    arr = list(map(int, input().split()))
    count = 0
    sum_arr = []
    for i in range(1<<N):
        a = []
        for j in range(N):
            if i & (1<<j):   
                a += [arr[j]]
                count += 1
        if len(a) == 3:
            sum_arr.append(sum(a))
    sum_arr.sort
    # 이진검색
