# 소수찾기

# 소수인지 판별하는 함수
# 소수면 1, 아니면 0 리턴
def check_prime_number(n):  
    if n == 1:
        return 0
    else:
        for i in range(2, n):
            if n % i == 0:
                return 0
        else:
            return 1        

count = 0
T = int(input())
num = list(map(int, input().split()))
for i in num:
    if check_prime_number(i) == 0:
        pass
    else:
        count += 1
print(count)
    

    
    
# def is_prime_number(number):
#     if number == 2:
#         return 1
#     elif number > 2:
#         for i in range(2,number):
#             if number % i == 0:
#                 return 0
#     else:
#         return 1
        
        
# count = 0
# T = int(input()) 
# for test_case in range(1, T + 1):
#     number = list(map(int, input().split()))
#     for i in number:
#         if is_prime_number(i) == 1:
#             count += 1
#     print(count)

            