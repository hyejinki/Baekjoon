def decomposition(N):                   # 분해합 구하는 함수
    num = map(int, list(str(N)))        # N % 10
    sum_N = N + sum(num)
    return sum_N
ans = 0
N = int(input())
for i in range(N):              # N-1까지
    if decomposition(i) == N:   # i의 분해합 == N 이라면 i가 N의 생성자!
        ans = i                 # ans에 대입
        break
print(ans)
