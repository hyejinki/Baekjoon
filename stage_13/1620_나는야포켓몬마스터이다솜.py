N, M = map(int, input().split())
arr1 = [input() for _ in range(N)]


for _ in range(M):
    dasom = input()
    for j in range(N):
        if '0' < dasom[0] and dasom[0] < '9':
            if int(dasom) == j:
                print(arr1[j-1])
        else:
            if dasom == arr1[j]:
                print(j+1)