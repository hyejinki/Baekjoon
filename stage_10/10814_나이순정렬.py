# 나이순 정렬
# 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서

# sort메서드 자체가 안정정렬의 속성을 갖고 있음
# 안정정렬 -> 기존의 정렬 형태를 유지한 상태에서 정렬함.(입력 순서와 동)

N = int(input())
li_info = []
for test_case in range(N):
    info = input().split()
    li_info.append(info)

li_info.sort(key= lambda x: int(x[0])) # int를 안해줘서 계속 틀렸다.

for i in li_info:
    print(i[0], i[1])