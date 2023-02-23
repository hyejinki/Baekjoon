import sys
n = int(input())
stack = []
ans = ''
for _ in range(n):
    x = int(sys.stdin.readline())                
    for i in range(1, x+1):          # 스택 비어있으면
        stack.append(i)
        print('+')
    while ans != x:                             # x를 pop할 때까지
        if x > stack[-1]:                       # x가 스택 마지막 요소보다 크면
            for i in range(stack[-1] + 1, x+1): #  push
                stack.append(i)
            stack.pop()
        else:                           # 작거나 같으면
            while stack[-1] != x:
                ans = stack.pop()

print(ans)



'''
8
1 2 3 4 5 6 7 8


'''