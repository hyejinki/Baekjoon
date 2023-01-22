# 수 정렬하기 2
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 제한 조건 최대 수 만큼의 리스트를 미리 만들어 놓고 시작
k = 10000 + 1
num_list = [0] * k

# 입력 받은 숫자 mylist에 추가
N = int(input())
for _ in range(N):
    num = int(input())
    num_list[num] = 1

for i in range(k):
    if num_list[i] == 1:
        print (i)