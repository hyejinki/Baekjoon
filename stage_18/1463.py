# 처음에 하나씩 따져보면 규칙 찾을 수 있다
num = int(input())
dp = [0]*(num + 1)
dp[1] = 0
if num > 1:
    dp[2] = 1
    if num > 2:
        dp[3] = 1
        for i in range(4, num + 1):
            compare = []
            if i % 3 == 0:        # 3의 배수이면
                compare.append(dp[i // 3])  # 나눈 값의 dp값을 추가
            if i % 2 == 0:
                compare.append(dp[i // 2])  # 나눈 값의 dp값을 추가
            compare.append(dp[i - 1])       # 마이너스한 값
            dp[i] = min(compare) + 1
print(dp[num])

# 1 > 1
# 2 > 1
# 3 > 1
# 4 > 2 > 1
# 5 > 4 > 2 > 1
# 6 > 2 > 1
# 7 > 6 > 2 > 1
# 8 > 4 > 2 > 1
# 9 > 3 > 1
# 10 > 9 > 3 > 1
# 11> 10 > 9 > 3 > 1
# 12 > 4 > 2 > 1

