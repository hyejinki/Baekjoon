# 달팽이는 올라가고 싶다
import math
A, B, V = map(int, input().split())
# total_height = 0
# i = 1
# while True :
#     day_height = A 
#     night_height = B
#     total_height += day_height
#     if V <= (total_height):
#         break
#     total_height -= night_height
#     i += 1
# print (i) #시간초과
# 가장 많이 올라간 때는 낮
# 최종 높이는 V - B
i = (V-B)/(A-B)
print(math.ceil(i))