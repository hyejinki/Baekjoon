



def f(i):       # i 는 리스트 길이
    k = 0
    x = i - 1  # 인덱스 번호
    for t in range(2, i/2):
        while k != i / 2:
            if ans[x - t - k] == ans[x - k]:
                k += 1

