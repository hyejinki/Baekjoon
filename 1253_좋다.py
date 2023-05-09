import sys, copy

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

cnt = 0
for x in arr:
    temp = copy.deepcopy(arr)
    temp.remove(x)

    i = 0
    j = N - 2
    while i < j and j < N - 1:
        if temp[i] + temp[j] == x:
            cnt += 1
          
            break
        elif temp[i] + temp[j] < x:
            i += 1
        elif temp[i] + temp[j] > x:
            j -= 1
print(cnt)