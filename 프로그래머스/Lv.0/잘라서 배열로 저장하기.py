def solution(my_str, n):
    answer = []
    i=0
    if len(my_str) == n:
        return [my_str]
    
    for i in range((len(my_str)-1)//n):
        answer.append(my_str[n*i:n*(i+1)])
        
    answer.append(my_str[n*(i+1):])
    return answer
