# 색종이


T = int(input())
total_li = []
for test_case in range(1, T+1):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            xy = (i, j)
            total_li.append(xy)
 
print(len(set(total_li)))

