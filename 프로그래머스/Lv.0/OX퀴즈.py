def solution(quiz):
    answer = []
    for s in quiz:
        x,op,y,eq,z = s.split()
        
        if op == '+':
            answer.append('O' if int(x)+int(y)==int(z) else 'X')
        else:
            answer.append('O' if int(x)-int(y)==int(z) else 'X')
    return answer
