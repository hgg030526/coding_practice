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



#다른 풀이 : 문자는 공백으로
def solution(my_string):
    numbers = ''.join(i if i.isdigit() else ' ' for i in my_string)
    return sum(int(i) for i in numbers.split())
