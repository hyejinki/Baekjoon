# N, M = map(int, input().split())
# arr1 = [input() for _ in range(N)]
# arr2 = [input() for _ in range(M)]
# count = 0
# sample = {}

# for word in arr1:           # 집합에 있는 단어로 value가 1인 딕셔너리 만들고
#     sample[word] = 1

# for word in arr2:           # 검사해야 할 단어가 sample의 value == 1이라면 
#     if sample.get(word) == 1:
#         count += 1

# print(count)

N, M = map(int, input().split())
arr1 = [input() for _ in range(N)]
arr2 = [input() for _ in range(M)]
count = 0
sample = []

for word in arr1:           # 집합에 있는 단어로 value가 1인 딕셔너리 만들고
    sample[word] = 1

for word in arr2:           # 검사해야 할 단어가 sample의 value == 1이라면 
    if word in sample:
        count += 1

# print(count)

#메모리는 적고, 시간 약 5배 오래걸림
# N, M = map(int, input().split())
# arr1 = [input() for _ in range(N)]
# arr2 = [input() for _ in range(M)]
# count = 0
# sample = []

# for word in arr2:
#     if word in arr1:
#         count += 1

# print(count)