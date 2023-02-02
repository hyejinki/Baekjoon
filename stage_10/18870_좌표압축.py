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