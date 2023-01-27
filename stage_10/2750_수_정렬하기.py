# 수 정렬하기
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 정수 입력하면 num_list에 추가한다. sorted하고 언패킹 연산자 사용해서 
# 개행 붙여서 출력
 
N = int(input())
num_list = []
for _ in range(N):
    num = int(input())
    num_list.append(num)
print(*(sorted(num_list)), sep = '\n')  # unpacking operator