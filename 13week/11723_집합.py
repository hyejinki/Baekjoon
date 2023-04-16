import sys, copy

M = int(sys.stdin.readline())
S = set()
s1 = set()
for i in range(1, 21):
    s1.add(i)
for _ in range(M):
    temp = sys.stdin.readline().split()
    if 'all' in temp:           # all, empty인 입력이 한 자리라서 따로 빼줌
        S = copy.copy(s1)
    elif 'empty' in temp:
        S = set()
    else:
        order = temp[0]
        num = temp[-1]
        if order == 'add':       
                S.add(int(num))
        elif order == 'remove':
                S.discard(int(num))     # discard는 set안에 요소가 없더라도 오류가 안 남
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
        
