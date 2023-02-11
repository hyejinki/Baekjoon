# 리스트는 시간초과
N, M = map(int, input().split())
no_listen = set(input() for _ in range(N))
no_see = set(input() for _ in range(M))
count = 0
ans = set()
for name in no_listen:          # no_listen돌면서 no_see에 있는지 탐색
    if name in no_see:
        count += 1
        no_see.remove(name)     # 겹치는 건 다시 볼 필요 없으니 삭제
        ans.add(name)

print(count,*sorted(ans), sep='\n')



# N, M = map(int, input().split())
# dic_heard = {}
# dic_seen= {}
# for _ in range(N):
#     no_heard = input()
#     dic_heard[no_heard] = 1
# for _ in range(M):
#     no_seen = input()
#     dic_seen[no_seen] = 1               # 딕셔너리에 입력
# for name in dic_heard:
#     if name in dic_seen:
        
    
