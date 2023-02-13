T = int(input())
for i in range(T):
    s = input()
    stack = [0] * len(s)
    top = -1
    ans = 'YES'
    for i in s:
        if i == '(':                # '('는 push
            top += 1
            stack[top] = i
        else:
            if top > -1:
                if stack[top] == '(':   # 이전에 올바른 짝이었으면 pop
                    top -= 1
                else:
                    ans = 'NO'
            else:                   # 닫는 괄호가 남아있으면 NO
                ans = 'NO'
    else:                           # 여는 괄호가 남아있으면 NO
        if top > -1:
            ans = 'NO'

    print(ans)
            


