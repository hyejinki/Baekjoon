import sys

M = int(sys.stdin.readline())
S = set()
s1 = set()
for i in range(21):
    s1.add(i)
for _ in range(M):
    # order, num = map(str, sys.stdin.readline().split())
    # print(order, num)
    temp = sys.stdin.readline().split()
    if temp == 'all':
        S = s1[:]
    elif temp == 'empty':
        S = {}
    else:
        order = temp[0]
        num = temp[-1]
        if order == 'add':       
                S.add(int(num))
        elif order == 'remove':
                S.remove(int(num))
        elif order == 'check':
            if int(num) in S:
                print(1)
            else:
                print(0)
        elif order == 'toggle':
            if int(num) not in S:
                S.add(int(num))
            else:
                S.remove(int(num))
        
    
