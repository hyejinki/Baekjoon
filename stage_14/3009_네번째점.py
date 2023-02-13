coor = [list(map(int, input().split()))for _ in range(3)]
list1 = [coor[0][0], coor[1][0], coor[2][0]]
list2 = [coor[0][1], coor[1][1], coor[2][1]]
ans1 = {}
ans2 = {}
for i in range(3):
    if list1[i] not in ans1:
        ans1[list1[i]] = 1
    else:
        ans1[list1[i]] += 1 
    if list2[i] not in ans2:
        ans2[list2[i]] = 1
    else:
        ans2[list2[i]] += 1

print(*[key for key, value in ans1.items() if value ==1], end = ' ')
print(*[key for key, value in ans2.items() if value ==1])