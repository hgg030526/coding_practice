def solution(my_string):
    answer = 0
    n = ''
    for s in my_string:
        print(s)
        if s.isdigit():
            n += s
        else:
            answer += 0 if n == '' else int(n)
            n = ''

    if n != '':
        answer += int(n)

    return answer
