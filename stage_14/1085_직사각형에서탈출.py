x, y, w, h = map(int, input().split())
min = 1000
sample = [x, y, abs(x - w), abs(y - h)]
for i in sample:
    if i < min:
        min = i
print(min)