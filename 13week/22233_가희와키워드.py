import sys

N, M = map(int, sys.stdin.readline().split())
memo = set(sys.stdin.readline().strip() for _ in range(N))

for _ in range(M):
    for x in (sys.stdin.readline().rstrip().split(',')):
        memo.discard(x)
    print(len(memo))