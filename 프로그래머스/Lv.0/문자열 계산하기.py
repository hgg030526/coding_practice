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
