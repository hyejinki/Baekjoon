# 좌표정렬하기

# 2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, 
# x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.


# 입력 받은 N을 행의 크기로 2차 배열을 입력.
N = int(input())
list_coordi = [list(map(int, input().split())) for _ in range(N)]
# 람다를 사용해서 우선순위 정해줌
list_coordi.sort(key=lambda x : (x[0], x[1]))
for i in range(len(list_coordi)):
    print(list_coordi[i][0], list_coordi[i][1])

