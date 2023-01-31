# 피보나치 수 5
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...
# n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오

def fibonacci(n):
    if n == 0:
        return 0 
    elif n == 1:
        return 1    # 0, 1 일 때는 따로 처리
    else: 
        return (fibonacci(n - 2) + fibonacci(n - 1))

n = int(input())
print(fibonacci(n))
