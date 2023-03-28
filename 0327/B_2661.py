



def f(i):       # i 는 리스트 길이

    
    for t in range(2, i//2 + 1):
            # if ans[i][i - t - k - 1] == ans[i][i - k - 1]:
        if i-(2*t)-1 < 0:
            a = ans[i][i-1-t::-1]
        else:
            a = ans[i][i-1-t:i-(2*t)-1:-1]
        if ans[i][i-1:i-t-1:-1] == a:
            return 0
    return 1
    
N = (int(input()))
ans = ['0'] * 81
num = [i for i in range(81)]
ans[1] = '1'
ans[2] = '12'
ans[3] = '121'
if N > 3:
    x = 4
    i = 1
    while x <= N:
        if num[i] != int(ans[x-1][-1]):
            ans[x] = ans[x-1] + str(num[i])
            if f(x) == 1:
                x += 1
                i = 1
            else:
                i += 1
        else:
            i += 1

print(int(ans[N]))