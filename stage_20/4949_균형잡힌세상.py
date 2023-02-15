import sys

while True:
    string = (sys.stdin.readline())
    if string == '.\n':
        break
    else:
        stack = [0] * 100
        top = -1
        ans = 'yes'
        for x in string:
            if x == '(' or x == '[':        # 여는 괄호는 push
                top += 1
                stack[top] = x              
            if x == ')':                    # ')' 라면 스택이 비어있지 않은지, '('와 짝이 맞는지 확인
                if top > -1:
                    if stack[top] ==  '(':
                        top -= 1
                    else:
                        ans = 'no'
                else:
                    ans = 'no'
            elif x == ']':              # ']' 라면 스택이 비어있지 않은지, '['와 짝이 맞는지 확인
                if top > -1:
                    if stack[top] == '[':
                        top -= 1
                    else:
                        ans = 'no'
                else: 
                    ans = 'no'     
        else:                           #  괄호가 남아있으면 no
            if top > -1:
                ans = 'no'
        print(ans)