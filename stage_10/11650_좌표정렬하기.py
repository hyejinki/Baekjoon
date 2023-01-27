# 좌표정렬하기

# 2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, 
# x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

N = int(input())
list_x = []
list_coordi = [list(map(int, input().split())) for _ in range(N)]
list_coordi.sort()
for i in range(len(list_coordi) - 1):
    list_coordi[i][0] == list_coordi[i + 1][0]
    list_coordi.sort()  # 뒤에 나오는 값 수정해야됨
print(list_coordi)

# for 
# if list_coordi[0] == 
# for i in range(N):
#     list_x.append(list_coordi[i][0])

