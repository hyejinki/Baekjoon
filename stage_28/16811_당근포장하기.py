T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    Ci = list(map(int, input().split()))
    ans = [[]*3]            # 소, 중 대
    res = 0
    over = [0] * (31)          # 당근 크기를 인덱스로  개수를 key로

    for x in range(1, 31):
        over[x] = Ci.count(x)
    print(over)

    new = []
    for n in over:
        if n != 0:
            new.append(n)
    print(new)

    minV = 30000
    for i in range(N-2):
        for j in range(i+1, N-1):
            A = sum(new[0:i+1])
            B = sum(new[i+1:j+1])
            C = sum(new[j+1:N])
        if minV > (max(A, B, C) - min(A, B, C)):
            minV = (max(A, B, C) - min(A, B, C))

    for w in over:  # N // 2 초과하면 탈락
        if w > (N // 2):
            minV = -1

    print(minV)