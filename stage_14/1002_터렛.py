T = int(input())
for test_case in range(1, T+1):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    l = abs(x1 - x2)**2 + abs(y1 - y2)**2   # 두 좌표 사이 거리의 제곱
    if l == (r1 + r2)**2:       # 두 좌표 사이 거리가 r1+r2일 때
        print(1)
    elif l < (r1 + r2)**2:
        if abs(r1 - r2)**2 > l: 
            print(0)
        else:
            print(2)
    elif l > (r1 + r2)**2:
        print(-1)