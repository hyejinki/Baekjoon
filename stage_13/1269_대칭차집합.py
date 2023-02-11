import sys
A, B = map(int, sys.stdin.readline().split())
A_set = set(map(int, sys.stdin.readline().split()))      # set으로 입력받고
B_set = set(map(int, sys.stdin.readline().split()))
print(len(A_set - B_set) + len(B_set - A_set))  # 빼주고 길이 합