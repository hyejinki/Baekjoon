# 팩토리얼
# 0보다 크거나 같은 정수 N이 주어진다. 이때 N!을 출력하는 프로그램을 작성하시오

def factorial(N):
    if N == 0:
        return 1        # 0 이면 리턴 1
    return N * factorial(N - 1)

N = int(input())
print(factorial(N))