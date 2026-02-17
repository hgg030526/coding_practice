def solution(s):
    answer = ''
    for i in set(s):
        if s.count(i) == 1:
            answer += i
    return ''.join(sorted(answer))  # sorted(answer) 은 배열로 정렬해줌. 따라서 join()으로 합쳐줘야 문자열이 됨
