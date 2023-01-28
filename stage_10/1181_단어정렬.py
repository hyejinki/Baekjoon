# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라
# 정렬하는 프로그램을 작성하시오
# 1. 길이가 짧은 것부터
# 2. 길이가 같으면 사전 순으로

N = int(input())
word_list = []
for i in range(N):
    word_list.append(input())
word_list = list(set(word_list)) # 중복 제거
# 길이로 정렬, 알파벳으로 정렬
word_list.sort(key= lambda x: (len(x), x))
print(*word_list, sep='\n') # 요소만 한 줄씩 띄어서 출력