
string = input()
set_str = set()

for i in range(1, len(string)+1):       # 개수
    for j in range(len(string)-i+1):    # 시작 인덱스
        set_str.add(string[j:j+i])      # i만큼 밀면서 개수만큼
            
print(len(set_str))