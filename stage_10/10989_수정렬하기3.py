# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램 작성
# 1<= N <= 10,000,000

import sys
T = int(sys.stdin.readline())
li = [0]
for i in range(T):  
    N = int(sys.stdin.readline())
    if N >= li[i]:
        li.append(N)
    else:
        for j in range(len(li)):
            if N <=  li[j]:
                li.insert(j, N)
                break
            
print(li[1:])