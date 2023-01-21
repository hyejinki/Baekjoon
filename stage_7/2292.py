#벌집
# 1
# 2 3 4 5 6 7  -> 6
# 8 9 10 11 12 13 14 15 16 17 18 19 -> 12개
# 20 ~ 37 -> 18개
# 38 ~ 61 -> 24개


num = int(input())
i = j = 1
if num == 1:
    print(1)
elif num > j:
    while num > j:
        j += 6 * i
        i += 1
    print(i)

    
