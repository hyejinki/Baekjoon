import sys
N = int(sys.stdin.readline())
sang = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
card_list = list(map(int, sys.stdin.readline().split()))

dic_count = {}
for num in card_list:
    dic_count[num] = 0          # 상근이가 가지고 있는 카드를 key로 딕셔너리 만들어놓고
for num in sang:
    if num not in dic_count:    # 리스트의 숫자가 디렉토리에 없으면 
        dic_count[num] = 1      # 디렉토리에 num : 1 을 추가한다.
    else:
        dic_count[num] += 1      # 있다면, value + 1


for i in card_list:
    print(dic_count[i], end=' ')



# for i in arr:
#     counter[i] = arr.count(i)