def solution(my_string, letter):
    return ''.join(s for s in my_string if s != letter)


#다른 풀이 : replace 사용
def solution(my_string, letter):
    return my_string.replace(letter, '')
