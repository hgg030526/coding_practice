def solution(age):
    lst = 'abcdefghij'
    answer = ''.join([lst[int(n)] for n in str(age)])
    return answer
