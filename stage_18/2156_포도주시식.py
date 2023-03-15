N = int(input())
arr = [int(input()) for _ in range(N)]
dp = [0] * (N + 1)
dp[1] = arr[0]
if N > 1:
    dp[2] = arr[0] + arr[1]
if N > 2:
    for i in range(3, N + 1):
        # 계단 오르기에서 dp[i - 1]만 추가해줌
        dp[i] = max(dp[i - 1], dp[i - 2] + arr[i - 1], dp[i - 3] + arr[i - 2] + arr[i - 1])
print(max(dp))