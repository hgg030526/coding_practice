def solution(s):
    lst = s.split()
    answer, pre = 0, 0
    for i in lst:
        if i == 'Z':
            answer -= pre
        else:
            answer += int(i)
            pre = int(i)
    return answer


#isdigit으로 하려했지만 음의정수는 isdigit이 False로 됨
