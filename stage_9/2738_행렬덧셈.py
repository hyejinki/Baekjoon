# 행렬 덧셈

# N x M 크기의 배열을 my_list에 입력 받는다. 처음 받은 배열은 A라는 리스트에 저장해둔다.
# 이중for문으로 각 인덱스의 요소를 합하고 언패킹 연산자를 사용해서 출력

N, M = map(int, input().split())
A = []
for n in range(2):  # 2개의 배열
    mylist = [list(map(int, input().split())) for _ in range(N)] 
    if n == 0:
        A = mylist  # A에 저장해둠
for i in range(N):
    for j in range(M):
        A[i][j] += mylist[i][j] # A에 mylist를 더함
    print(*A[i])


