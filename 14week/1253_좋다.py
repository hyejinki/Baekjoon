import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
cnt = 0
# sum = set()
# for i in range(len(arr) - 1):
#     for j in range(i + 1, len(arr)):
#         if (arr[i] + arr[j]) <= max(arr):
#             sum.add((arr[i] + arr[j]))
# cnt = 0
# for x in arr:
#     if x in sum:
#         cnt += 1

for i in range(len(arr) -1):
    for j in range(i + 1, len(arr)):
        if arr[j] > arr[i]:
            break:





print(cnt)