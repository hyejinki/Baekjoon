# 두가지 형태의 체스판 먼저 만들어주기 
black = ['B','W','B','W','B','W','B','W']
white = ['W','B','W','B','W','B','W','B']
board1 = []
board2 = []
for i in range(8):
    if i % 2 == 0:
        board1.append(black)
        board2.append(white)
    else:
        board1.append(white)
        board2.append(black)

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
minV = 64                           
for i in range(N-7):                # 행의 시작                                                                
    for j in range(M-7):            # 열의 시작
        count1 = count2 = 0
        for k in range(i, i+8):         # 8개씩 옮겨가면서 볼거임
            for l in range(j, j+8):
                if arr[k][l] != board1[k-i][l-j]:   # board는 8X8로 정해져 있으니 -i, -j
                    count1 += 1
                elif arr[k][l] != board2[k-i][l-j]:
                    count2 += 1
        if minV > min(count1, count2):
            minV = min(count1, count2)  # 카운트 중 제일 작은 값

print(minV)