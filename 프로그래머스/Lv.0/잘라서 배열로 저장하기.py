def solution(my_str, n):
    answer = []
    i=0
    if len(my_str) == n:
        return [my_str]
    
    for i in range((len(my_str)-1)//n):
        answer.append(my_str[n*i:n*(i+1)])
        
    answer.append(my_str[n*(i+1):])
    return answer

#두번째 풀이
def solution(my_str, n):
    answer,i,end_i = [],0,(len(my_str)-1)//n
    
    while i < end_i:
        answer.append(my_str[n*i:n*(i+1)])
        i += 1
        
    answer.append(my_str[n*end_i:])
        
    return answer


#다른 풀이 : 슬라이싱은 초과해도 오류가 발생하지 않는다
def solution(my_str, n):
    return [my_str[i:i+n] for i in range(0,len(my_str),n)]
