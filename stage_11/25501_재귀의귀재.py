# 팰린드롬인지 판별하는 함수를 만들고 더불어 판별하는 과정에서 recursion 함수를 몇 번 호출하는지 셀 것이다.
def isPalindrome(string):
    reversed_str = string[::-1]
    if string == reversed_str:
        return 1
    else:
        return 0

