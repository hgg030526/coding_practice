def solution(my_string):
    lst = my_string.split()
    numbers,operators = [],[]

    for i in lst:
        if i in ['+','-']:
            operators.append(i)
        else:
            numbers.append(int(i))

    answer = numbers[0]

    for i,op in enumerate(operators):
        if op == '+':
            answer += numbers[i+1]
        else:
            answer -= numbers[i+1]

    return answer


#다른 풀이 : 9 - 2 를 9 + (-2) 로 푸는 방법
def solution(my_string):
    return sum(int(i) for i in my_string.replace(' - ',' + -').split(' + '))
