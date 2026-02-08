def solution(my_string):
    answer = ''
    for i in my_string:
        if i==i.upper():  #i.isupper()
            answer += i.lower()
        else:
            answer += i.upper()
    return answer
