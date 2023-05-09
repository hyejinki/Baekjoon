def check(n, sum1, sum2):
    global lion
    
    if  n == info[0]:
        return -1
    else:
        for i in range(11):
            if info[i] == n:
                check(n, sum1+(10-i), sum2)
            else:
                if info[i] != 0:
                    check(n, sum1, sum2+(10-i))     # 더하냐 
                    lion.append(info[i]+1)
                    check(n, sum1+(10-i), sum2)        # 넘어가냐
                    lion.append(0)



n= 5
info = [2,1,1,1,0,0,0,0,0,0,0]
lion = []
score = 0
check(5, 0, 0)
print(lion)

# 배열 안의 숫자는 상관 없어
#  갖느냐 못 갖느냐. 완탐
#  이기는 경우 중 가장 큰 점수 차이/ 가장 작은 점수의 횟수

        
   

