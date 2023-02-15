import sys

while True:
    string = (sys.stdin.readline())
    stack = [0]*100
    top = -1
    ans = 'yes'
    for x in string:
        if x == '(' or x == '[':
            top += 1
            stack[top] = x
        if x == ')':
            if top > -1:
                if stack[top] ==  '(':
                    top -= 1
                else:

        elif x == ']':
            if stack[top] == '[':
                top -= 1

    if string == ['.']:
        break
