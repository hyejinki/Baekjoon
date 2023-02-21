import sys
from collections import deque
T = int(sys.stdin.readline())
for test_case in range(1, T + 1):
    N, M = map(int, sys.stdin.readline().strip().split())
    arr = list(map(int, sys.stdin.readline().strip().split()))
    imp = deque()
    i = 0
    for x in arr:               # 인덱스와 중요도 튜플로 imp에 넣음
        imp.append((i, x))
        i += 1

    count = 0
    while True:
        maxV = 0
        for i in range(len(imp)):           # imp의 중요도 max값 구하기
            if imp[i][1] > maxV:
                maxV = imp[i][1]
        if maxV == imp[0][1]:   # 맨 앞에 가장 중요한 문서라면
            if imp[0][0] == M:  # 근데 그게 원하는 인덱스(==M)라면
                count += 1
                break
            else:
                imp.popleft()   # M아니면 pop
                count += 1
        else:
            imp.append(imp.popleft())  # 중요한 거 아니면 맨 뒤로 보내
    print(count)