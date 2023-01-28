# 2차원 평면 위의 점 N개가 주어진다. 
# y를 기준으로, 같으면 x가 증가하는 순서

# 입력 받은 N을 행의 크기로 2차 배열을 입력.
N = int(input())
list_coordi = [list(map(int, input().split())) for _ in range(N)]
# 람다를 사용해서 우선순위 정해줌 (11650이랑 순서만 바꿔줌)
list_coordi.sort(key=lambda x : (x[1], x[0]))
for i in range(len(list_coordi)):
    print(list_coordi[i][0], list_coordi[i][1])

