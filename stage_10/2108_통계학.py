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
    new_list = []
    list_max = []
    for i in num_list:
        list_max.append(abs(i))
        max_value = max(list_max) # 리스트에서 가장 큰 값
    list_value = [0]*(max_value) #가장 큰 값 만큼의 개수를 가진 리스트 생성
    for j in num_list:
        list_value[j] += 1  #해당 인덱스에 개수만큼 카운트
# 0이 아닌 값을 가진 인덱스만 또 따로 new리스트에 추가
    for k in list_value:    
        if k != 0:
            new_list.append(k)
# 뉴 리스트 길이가 1이라면 == 입력 숫자가 하나밖에 없었다면            
    if len(new_list) == 1:
        return num_list[0]
# 최빈수가 2개 이상이면 두번째로 작은 값을 출력
    elif len(new_list) >= 2:    
        sorted(new_list)


# 범위 함수
def ran(num_list):
    n = max(num_list) - min(num_list)
    return n

num_list = []
T = int(input())
for test_case in range(1, T + 1):
    num = int(input())
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