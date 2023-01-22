# 골드바흐의 추측은 유명한 정수론의 미해결 문제로, 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다는 것이다
# 제한 조건에 맞춰 10000이하의 소수를 미리 찾아 놓는다.
n = 10000 + 1
prime_list = [1] * n
for i in range(n):
    if i == 0 or i == 1:
        prime_list[i] = 0
    else:
        for num in range(2, int(i**0.5 + 1)):
            if i % num == 0:
                prime_list[i] = 0
                break

T = int(input()) 
dict_ans = {}
for test_case in range(1, T + 1):
    N = int(input())
    li_num = [k for k in range(N) if prime_list[k]]
    for i in li_num:       
        for j in li_num:
            if i + j == N:
                dict_ans[(i, j)] = i * j
    max_ans = max(dict_ans, key = dict_ans.get)
    ans = ' '.join(map(str, max_ans))
    print(ans)
        
      
