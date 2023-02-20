n = int(input())
stack = []
ans = ''
val = 0                                 # 현재값
for _ in range(n):
    num = int(input())
    if num > val:                       # 입력값이 현재값보다 크면
        for i in range(1, num + 1):
            stack.append(i)             # push
            ans += '+'
            val = stack.pop(num)        # val = 현재값 
    else:
        val = stack.pop(num)
    
    

    

