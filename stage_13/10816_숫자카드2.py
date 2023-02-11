import sys
N = int(sys.stdin.readline())
sanggeun = list(map(int, sys.stdin.readline().strip().split()))
M = int(sys.stdin.readline())
num_card = list(map(int, sys.stdin.readline().strip().split()))

# 상근이 카드가 num_card에 몇 개 있는지?
ans_dic = {}
for num in sanggeun:
    if num not in ans_dic:
        ans_dic[num] = 1
    else:
        ans_dic[num] += 1

for i in num_card:
    print(ans_dic.get(i, 0), end=' ')