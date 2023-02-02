# 좌표 압축

# 시간초과
# 리스트 복사해서 하나는 set해줌
# import copy
# N = int(input())

# ans = []
# li_x = list(map(int, input().split()))
# li_copy = set(copy.deepcopy(li_x))


# for x in li_x:
#     count = 0
#     for c in li_copy:
#         if x > c:
#             count += 1
#     ans.append(count)

# print(*ans)

<<<<<<< HEAD
# 리스트 복사해서 하나 set하고 인덱스 번호 

# import copy
# N = int(input())

# ans = []
# li_x = list(map(int, input().split()))      # 오리지널
# li_copy = sorted(copy.deepcopy(li_x))       # 복사



# for n in li_x:
# #     count = 0
# #     for i in set(li_copy):
# #         if i < n:
# #             count += 1
# #     ans.append(count)            
#     # N보다 작은 수.
#     ans.append(list(set(li_copy)).index(n))

# print(*ans)


N = int(input())
arr = list(map(int, input().split()))
new_arr = sorted(list(set(arr))) # 중복 제거 -> 리스트화 -> 정렬
ans = []
for num in arr:
    ans.append(new_arr.index(num))  # 정렬한 리스트의 인덱스 넘버 == 보다 작은 수의 개수
print(*ans)
=======
import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
new_arr = sorted(list(set(arr))) # 중복 제거 -> 리스트화 -> 정렬
ans = {}
for i in range(len(new_arr)):   # 딕셔너리에 new_arr의 값을 key로
    ans[new_arr[i]] = i         # 해당 인덱스(자신보다 작은 값의 개수)를 value로 넣음

for i in arr:
    print(ans[i], end=' ')
>>>>>>> f5928724c0c155f041da6d6351156cdf0193410a
