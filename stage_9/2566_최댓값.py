# 최댓값

# my_list = [list(map(int, input().split())) for _ in range(9)]
# max_value = -1
# for i in range(9):
#     for j in range(9):
#         if max_value < max(my_list[i]):
#             max_value = max(my_list[i])
#         if max_value == my_list[i][j]:
#             row = i + 1
#             col = j + 1

# print(max_value)
# print(row, col) 

# 9x9 행렬 입력 받고 한 줄 씩 가장 큰 값을 max_value에 할당(덮어쓰기)
# 가장 큰 값 찾아서 출력하고 그 값의 자리를 찾아 인덱스 출력

my_list = [list(map(int, input().split())) for _ in range(9)]
max_value = 0
for i in range(9):
    if max_value < (max(my_list[i])):
        max_value = max(my_list[i])
print(max_value)   # 최댓값
for i in range(9):
    for j in range(9):
        if max_value == my_list[i][j]:   # 인덱스 찾기
            print(i + 1, j + 1)
    