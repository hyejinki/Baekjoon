# 10 15
# 5 1 3 5 10 7 4 9 2 8

N, S = map(int, input().split())
arr = list(map(int, input().split()))

head, tail = 0, 1
min = N

while head < N:
    if head >= S:
        pritn(1)
        break
        
    else:
        sum = 0
        while sum < S:
            