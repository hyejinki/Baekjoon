# 소트인사이드
# 배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.

N = int(input())
list_N = []
a = []
for i in str(N):
    list_N.append(i)
    
print(*(sorted(list_N)[::-1]), sep = '')