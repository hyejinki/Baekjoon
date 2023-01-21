# 소수 구하기

M, N = map(int, input().split())
sum_list = []
for num in range(M, N+1):
    prime_number = 1  # flag처럼 사용할 것. 1이면 소수이다.
    if num > 1:
        for i in range(2, int(num**0.5) + 1):   # number까지 돌릴 필요 없이 제곱근까지만
            if num % i == 0:  
                prime_number = 0    # 나눠지면 0으로 바뀌고 브레이크
                break
        if prime_number != 0:
            sum_list.append(num)   
# 2581에서 출력만 수정함
for i in sum_list:
    print(i)
