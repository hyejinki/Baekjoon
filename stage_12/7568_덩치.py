

N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]
li_ans = []
for i in range(N):
    ans = 1             # 본인 포함
    for j in range(N):
        if info[i][0] < info[j][0] and info[i][1] < info[j][1]:     # 둘 다 크면
            ans += 1
    li_ans.append(ans)
print(*li_ans)
        


# 5
# 55 185
# 58 183
# 88 186
# 60 175
# 46 155