def solution(polynomial):
    a,b,a_n,b_n = 0,0,0,0
    
    for term in polynomial.split(' + '):
        if 'x' in term:
            a_n += 1
            if term == 'x':
                a += 1
            else:
                a += int(term[:-1])
        else:
            b_n += 1
            b += int(term)
    
    if a == 1:  #일차항의 계수가 1인 경우는 생략해야하기 때문
        a = ''
        
    if a_n*b_n != 0:
        answer = str(a) + 'x' + ' + ' + str(b)
    elif a_n == 0:
        answer = str(b)
    else:
        answer = str(a) + 'x'
        
    return answer



#간단하게
def solution(polynomial):
    a,b = 0,0
    
    for term in polynomial.split(' + '):
        if 'x' in term:
            a += 1 if term == 'x' else int(term[:-1])
        else:
            b += int(term)
    
    if a == 0:
        answer = str(b)
    elif a == 1:
        answer = 'x + ' + str(b) if b != 0 else 'x'
    else:
        answer = f'{a}x + {b}' if b != 0 else f'{a}x'
        
    return answer
