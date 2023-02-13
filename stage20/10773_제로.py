K = int(input())
stack = [0] * K             # K 크기 만큼의 스택
top = -1
for i in range(K):
    num = int(input())
    if num != 0:                # 0이 아닌 수는  push
        top += 1
        stack[top] = num
    else:                       # 0 이면 top 낮춰주고
        top -= 1
print(sum(stack[:top+1]))       # 마지막 top까지의 합