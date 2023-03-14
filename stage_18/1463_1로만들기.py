# 처음에 하나씩 따져보면 규칙 찾을 수 있다
num = int(input())
dp = []*(num + 1)
compare = []
dp[1] = 1
dp[2] = 1
dp[3] = 1
for i in range(4, num + 1):
    if num % 3 == 0:        # 3의 배수이면
        compare.append(dp[num // 3])
    if num % 2 == 0:
        compare.append(dp[num // 2])
    compare.append(dp[num - 1])

print(min(compare) + 1)

#
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

