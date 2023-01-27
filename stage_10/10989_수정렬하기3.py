# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램 작성
# 1<= N <= 10,000,000

# 입력 받을 때마다 작은지 큰지 비교
# import sys
# T = int(sys.stdin.readline())
# li = [0]
# for i in range(T):  
#     N = int(sys.stdin.readline())
#     if N >= li[i]:
#         li.append(N)
#     else:
#         for j in range(len(li)):
#             if N <=  li[j]:
#                 li.insert(j, N)
#                 break
            
# print(li[1:])

# 퀵 정렬
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
   

    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for i in arr:
        if i < pivot:
            lesser_arr.append(i)
        elif i > pivot:
            greater_arr.append(i)
        else:
            equal_arr.append(i)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)

T = int(input())
li = []
for i in range(T):
    N = int(input())
    li.append(N) # 입력한 숫자 리스트에 넣음


print(*quick_sort(li), sep = '\n')