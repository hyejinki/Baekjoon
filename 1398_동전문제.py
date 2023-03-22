# 두 개씩 끊어서 생각하면 된다는 힌트 보고 풀었습니다
# dp
coin = [1, 10, 25] # 이 형태에서 자릿수만 다름

T = int(input())
for _ in range(T):
    N = int(input())
    ans = 0
    dp = [10**15 + 1 for _ in range(100)]
    dp[0] = 0
    while N:
        n = N % 100     # 두 자리만 보려고 
        for c in coin:    # 리스트에 있는 c
            for i in range(c, n + 1):
                dp[i] = min(dp[i], dp[i - c] + 1)
        ans += dp[n]        # 누적 합
        N //= 100    # 뒤에 두 개 자르고 다시 올려

    print(ans)

    # while N:
    #     ans += dp[N % 100]
    #     N //= 100
    # print(ans)