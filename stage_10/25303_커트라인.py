# 커트라인

T, cut = map(int, input().split())
li_score = list(map(int, input().split()))

print(sorted(li_score)[T - cut])    # 끝에서 cut번째
