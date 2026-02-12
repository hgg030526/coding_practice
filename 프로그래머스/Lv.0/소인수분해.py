def solution(n):
    answer = []
    i = 2
    while n != 1:
        while n%i == 0:
            n //= i
            answer.append(i)
        i += 1
    return sorted(set(answer)) #set()는 정렬이 안됨 따라서 list()가 아닌 sorted()로 묶어주기! 
