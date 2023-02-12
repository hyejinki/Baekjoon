import sys
N = int(sys.stdin.readline())
sanggeun = list(map(int, sys.stdin.readline().strip().split()))
M = int(sys.stdin.readline())
num_card = list(map(int, sys.stdin.readline().strip().split()))

# 상근이 딕셔너리 만들기
ans_dic = {}
for num in sanggeun:
    if num not in ans_dic:
        ans_dic[num] = 1
    else:
        ans_dic[num] += 1

for i in num_card:              # 체크할 숫자를 key로 상근이 딕셔너리 vlaue출력
    print(ans_dic.get(i, 0), end=' ')   # key가 없으면 0 출력