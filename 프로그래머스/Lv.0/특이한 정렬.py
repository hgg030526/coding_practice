def solution(numlist, n):
    numlist.sort(reverse = True)
    return sorted(numlist,key = lambda x:abs(x-n))

# 다른 풀이 : lambda를 사용 + 2차 조건까지 주기(abs(x-n) 가 같을 경우 n-x가 작은 거 먼저
def solution(numlist, n):
    return sorted(numlist,key = lambda x:(abs(x-n),n-x))
