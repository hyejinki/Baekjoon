# 소수 찾기
def is_prime_number(number):
    if number == 2:
        return 1
    elif number > 2:
        for i in range(2,number):
            if number % i == 0:
                return 0
    else:
        return 1
        
        
count = 0
T = int(input()) 
for test_case in range(1, T + 1):
    number = list(map(int, input().split()))
    for i in number:
        if is_prime_number(i) == 1:
            count += 1
    print(count)

            

    

