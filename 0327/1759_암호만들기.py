def f(i, n, k):
    cnt = 0
    flag = 1
    if i == k:
        for i in range(k - 1):
            if p[i] > p[i + 1]:
                flag = 0
                break
        if flag == 1:
            for x in p:

                if x in v :
                    cnt += 1
            if 1 <= cnt <= k - 2:
                print(*p)

    else:
        for j in range(C):      # k가 아님에 주의
            if used[j] == 0:
                used[j] = 1
                p[i] = A[j]
                f(i + 1, n, k)
                used[j] = 0

v = ['a', 'e', 'i', 'o', 'u']
L, C = map(int, input().split())
A = list(input().split())

A.sort()

p = [0] * L
used = [0] * C
f(0, C, L)