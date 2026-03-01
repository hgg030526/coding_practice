def find_factors(n):
    factor = []
    i = 2
    while n != 1:
        while n%i == 0:
            factor.append(i)
            n //= i
        i += 1
        
    return factor


def solution(a, b):
    answer = 0
    
    for i in find_factors(a):
        if b%i == 0:
            b //= i
            
    return 1 if len(set(find_factors(b)) | set([2,5])) == 2 else 2

# 다른 풀이 : 최대공약수 활용하기
