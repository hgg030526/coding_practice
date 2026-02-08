def solution(strlist):
    return [len(s) for s in strlist]


#다른 풀이 : map() 사용
def solution(strlist):
    answer = list(map(len, strlist))
    return answer
