def solution(n):
    answer = 0
    for i in range(4,n+1):
        if i%2 == 0:
            answer += 1
            continue
            
        for n in range(3,int(i**0.5)+1):
            if i%n==0:
                answer += 1
                break
                
    return answer


#짧은 버전
def solution(n):
    answer = 0
    for i in range(4,n+1):
        for n in range(2,int(i**0.5)+1):
            if i%n==0:
                answer += 1
                break
                
    return answer
