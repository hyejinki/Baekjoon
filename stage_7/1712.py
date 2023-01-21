# A만원 고정 비용
# 재료비 + 인건비 등 = B만원 가변 비용

A, B, C = map(int, input().split())
if B >= C:  #손익분기점 없는 경우
    print(-1)
else:
    print(A//(C-B)+1) # A + B * i = C * i
        
