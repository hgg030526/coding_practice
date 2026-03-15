def solution(quiz):
    answer = []
    for s in quiz:
        x,op,y,eq,z = s.split()  # eq는 안쓰는 변수이므로 '_'로 써도 됨
        
        if op == '+':
            answer.append('O' if int(x)+int(y)==int(z) else 'X')
        else:
            answer.append('O' if int(x)-int(y)==int(z) else 'X')
    return answer
