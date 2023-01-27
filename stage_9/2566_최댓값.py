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

# 9x9 행렬 입력 받고

my_list = [list(map(int, input().split())) for _ in range(9)]
max_value = 0
for i in range(9):
    if max_value < (max(my_list[i])):
        max_value = max(my_list[i])
print(max_value)
for i in range(9):
    for j in range(9):
        if max_value == my_list[i][j]:
            print(i + 1, j + 1)
    