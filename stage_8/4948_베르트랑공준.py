# 베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다.
# 숫자 입력 받고 리스트에 넣음
# num_list = []
# while True:
#     N = int(input())
#     num_list.append(N)
#     if N == 0: break

# prime_num = 1
# count = 0
# for i in num_list:
#     if i == 0:
#         break
#     count = 0
#     for num in range(i + 1, 2*i + 1):   # 자기보다 크고 2배보다 작거나 같은 
#         for j in range(2, int(num**0.5) + 1):   # num까지 돌릴 필요 없이 제곱근까지만
#             prime_num = 1  # flag처럼 사용할 것. 1이면 소수이다.
#             if num % j == 0:  
#                 prime_num = 0    # 나눠지면 0으로 바뀌고 브레이크
#                 break
#         if prime_num != 0:
#             count += 1   
#     print(count)


# 입력 최대가 123456 -> 2배 246912
# 시간 단축을 위해서 최댓값까지의 소수 유무를 밀 다 찾아놓고 시작
n = 123456 * 2 + 1   # 인덱스 번호 맞춰주려고 +1
num_list = [1] * n   # n개만큼 자리를 만들어 준다
for i in range(n):
    if i == 0 or i == 1:
        num_list[i] = 0    # 소수가 아닌 건 0
    else:
        for num in range(2, int(i**0.5 + 1)):    # 제곱근까지만 비교
            if i % num == 0:
                num_list[i] = 0    # 소수가 아닌 것만 0으로 바꾼다
                break
N_list = []
while True:
    N = int(input())
    N_list.append(N)
    if N == 0:    # 0 이면 그만
        break
for k in N_list:    
    count = 0    
    if k == 0:
        break    
    for i in range(k + 1, 2*k + 1):    
        count += num_list[i]    # num_list는 0과 1로만 이루어져있다. 소수라면 1, 아니면 0 따라서 구간 내 카운트의 의미
    print(count)
    
    
# 1
# 10
# 13
# 100
# 1000
# 10000
# 100000