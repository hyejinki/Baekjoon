# ACM 호텔
T = int(input()) 
for test_case in range(1, T + 1):
    X = 0
    H, W, N = map(int, input().split())
    
    for i in range(1, W + 1):   # 방 개수
        for j in range(1, H + 1):   # 층수
            X += 1  # 카운트해서 N이 되면 끝.
            if X == N:  
                break
        if X == N:
            break    
    if i <= 9 :
        print(j,0,i,sep='')     # j = 층 / i = 호수                
    else :
        print(j, i, sep='')
                
    
                