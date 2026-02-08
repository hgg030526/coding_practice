def solution(my_string, n):
    answer = ''
    for s in my_string:
        answer += s*n
    return answer


#다른 풀이 : join사용
def solution(my_string, n):
    return ''.join(i*n for i in my_string) # i*n for i in my_string 는 list comprehension으로 type이 list임
