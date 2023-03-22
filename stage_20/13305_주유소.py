N = int(input())
d = list(map(int, input().split()))
cost = list(map(int, input().split()))
sum = 0
i = 0
while i < N - 1:
    if cost[i] >= cost[i + 1]:
        sum += cost[i] * d[i]
        i += 1
    else:
        j = i + 1
        while j < N - 1 :
            if cost[i] >= cost[j]:   
                break  
            sum += cost[i] * d[j]
            j += 1
        i += j    

print(sum)
        