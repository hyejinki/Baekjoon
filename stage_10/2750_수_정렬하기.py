# 수 정렬하기
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

N = int(input())
num_list = []
for i in range(N):
    num = int(input())
    num_list.append(num)
print(*(sorted(num_list)), sep = '\n')  # unpacking operator