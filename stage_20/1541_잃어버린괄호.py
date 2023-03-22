'''
form = input()

new = []
for char in form:
    if '0' <= char and char <= '9':
        new.append(int(char))
    else:
        new.append(char)
cnt = 0
num = []
a = 0
res = []
for i in new:
    if type(i) == int:
        cnt += 1
        num.append(i)
    else: 
        for j in num:
            a += j * 10 * (cnt - 1)
            cnt -= 1
        res.append(a)
        res.append(i)
        
        
print(res)
# '''

# import sys

# word = list(map(str, input().split('-')))
# print(word)
# check = list(map(int, word[0].split('+')))
# ans = sum(check)
# print(check)
# print(ans)

stack = []
stack2 = []
num = ''
sig = input()
s = len(sig)
for i in range(s):
    if sig[i].isnumeric():
        num += sig[i]
        if i == s-1:
            stack2.append(int(num))
    else:
        stack.append(sig[i])
        stack2.append(int(num))
        num = ''

# print(stack)
# print(stack2)

# -나오면 괄호 시작(+나오는 동안) 즉, 다시 - 나오면 괄호 끝
n = stack2.pop()
ans = n
while stack2:
    n = stack2.pop()
    sign = stack.pop()
    if sign == '+':
        ans += n
    else:
        if len(stack) != 0 and stack[-1] == '-':
            n += ans
        else:
            n -= ans
        ans = n

print(ans)