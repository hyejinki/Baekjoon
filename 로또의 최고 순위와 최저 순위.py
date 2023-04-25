lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]

score = {6:1, 5:2, 4:3, 3:4, 2:5}

cnt_zero = 0
cnt_cor = 0
for x in lottos:
    for y in win_nums:
        if x == 0:
            cnt_zero += 1
            break
        else:
            if x == y:
                cnt_cor += 1
            
# 최고순위는 
answer = []
for i in [cnt_zero + cnt_cor, cnt_cor]:
    if i in score:
        answer.append(score[i])
    else:
        answer.append(6)
        


    
print(answer)