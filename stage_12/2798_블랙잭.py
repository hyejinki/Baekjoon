# # 시간초과
# N, M = map(int, input().split())
# arr = list(map(int, input().split()))

# sum_arr = []
# # 부분집합
# minV = 300000
# for i in range(1<<N):
#     a = []
#     for j in range(N):
#         if i & (1<<j):   
#             a += [arr[j]]
#     if len(a) == 3:             # 크기가 3개인 것
#         sum_arr.append(sum(a))

# for i in sum_arr:
#     if i == M:
#         ans = i
#         break
#     else:
#         if abs(i - M) < minV:
#             minV = abs(i - M)
#             ans = i 
# print(ans)    

N, M = map(int, input().split())
arr = list(map(int, input().split()))
sum_arr = 0         # 카드 3장 더한 값
ans = []            # 더한 값들을 넣어줄 리스트
for i in range(len(arr)-2):     # 맨 뒤에서 3번째까지
    for j in range(i+1, len(arr)-1):    # i보다 하나 크고 뒤에서 두번째까지
        for k in range(j+1,len(arr)):   # j보다 하나 크고 맨 뒤까지
            sum_arr = arr[i] + arr[j] + arr[k]
            if sum_arr <= M:            # M보다 작거나 같아? 그럼 추가
                ans.append(sum_arr)
ans.sort()      # 정렬하고 마지막 값 출력
print(ans[-1])