
def hanoitower(n, start, mid, to):
    if n == 1:                           # 하나만 옮길 때
        print(start, to)       
        return
    hanoitower(n-1, start, to, mid)     # 경유하는 경우
    print(start, to)
    hanoitower(n-1, mid, start, to)     # 경유지에서 목적지까지
    

N = int(input())
print(2**N - 1)         # 횟수 
hanoitower(N, 1, 2, 3)