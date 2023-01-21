# # 소수



# import time
# start_time = time.time()
# 함수를 따로 빼면 시간이 너무 오래 걸려서 전면 수정.
sum_list = []
M = int(input())
N = int(input())
for num in range(M, N+1):
    prime_num = 1  # flag처럼 사용할 것. 1이면 소수이다.
    if num > 1:
        for i in range(2, int(num**0.5) + 1):   # number까지 돌릴 필요 없이 절반까지만
            if num % i == 0:  
                prime_num = 0    # 나눠지면 0으로 바뀌고 브레이크
                break
        if prime_num != 0:
            sum_list.append(num)   

if sum_list == []:
    print(-1)
else:
    print(sum(sum_list))
    print(sum_list[0])


# end_time = time.time()
# print(end_time - start_time)


