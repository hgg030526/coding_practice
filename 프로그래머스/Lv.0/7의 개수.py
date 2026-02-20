def solution(array):
    answer = 0
    return ''.join(str(i) for i in array).count('7')


#다른 풀이 : str(배열) 사용 : [7, 17] -> '[7, 17]' 배열 자체가 문자열이 됨
def solution(array):
    return str(array).count('7')
