# 좌표정렬하기

# 2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, 
# x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

N = int(input())
list_x = []
list_coor = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    list_x.append(list_coor[i][0])

