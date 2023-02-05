
def hanoitower(n, start, mid, to):
    if n == 1:
        print(start, to)
        return
    hanoitower(n-1, start, to, mid)
    print(start, to)
    hanoitower(n-1, mid, start, to)
    

N = int(input())
print(2**N - 1)
hanoitower(N, 1, 2, 3)