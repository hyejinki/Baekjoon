# 팰린드롬인지 판별하는 함수를 만들고 더불어 판별하는 과정에서 recursion 함수를 몇 번 호출하는지 셀 것이다.
# def isPalindrome(string):
#     i = 0
#     reversed_str = string[::-1]
#     if string == reversed_str:
#         return 1
#     else:
#         return 0
#     isPalindrome()


def recursion(s, l, r): # 재귀를 돌 때마다 l이 0에서부터 1만큼 커진다.
    
    if l >= r: 
        return (1, l + 1)      # 리턴값 추가 l + 1
    elif s[l] != s[r]:         # 다른 거 찾으면 return 0
        return (0, l + 1)
    else: 
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)    # 인자는 처음문자, 0, 마지막 문자

T = int(input())
for test_case in range(T):
    S = input()
    isPalindrome(S)
    print(*isPalindrome(S))