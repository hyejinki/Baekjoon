# 통계학
# 산술평균 함수
def mean(num_list):
    n = (sum(num_list) / len(num_list))
    return (round(n))

# 중앙값 함수
def median(num_list):
    n = len(num_list) / 2 
    num = sorted(num_list)[int(n)]
    return num

# 최빈값 함수
def mode(num_list):
    dic_count = {}
    for num in num_list:
        if num not in dic_count:    # 리스트의 숫자가 디렉토리에 없으면 
            dic_count[num] = 1      # 디렉토리에 num : 1 을 추가한다.
        else:
            dic_count[num] += 1      # 있다면, value + 1
    # 가장 큰 value == key가 최빈수
    max_key = max(dic_count, key=dic_count.get)
    return max_key


# 범위 함수
def ran(num_list):
    n = max(num_list) - min(num_list)
    return n


import sys
num_list = []
T = int(sys.stdin.readline())
for test_case in range(1, T + 1):
    num = int(sys.stdin.readline())
    num_list.append(num)

print(mean(num_list))
print(median(num_list))
print(mode(num_list))
print(ran(num_list))

# 5
# -1
# -2
# -3
# -1
# -2